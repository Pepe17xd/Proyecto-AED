"""Optimiza el guion de voz mediante un modelo local de Ollama."""

from __future__ import annotations

import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from dotenv import load_dotenv

from narracion_utils import GUION_FINAL, GUION_OPTIMIZADO, extraer_secciones, escribir_secciones


# ``override=False`` preserva valores configurados por el sistema o la sesión.
load_dotenv(GUION_FINAL.parent.parent / ".env", override=False)
URL_OLLAMA = os.getenv("OLLAMA_URL", "http://localhost:11434")
MODELO_OLLAMA = os.getenv("OLLAMA_MODEL", "").strip()
ARCHIVO_PROMPT = GUION_FINAL.parent / "prompts_narracion.md"


def obtener_modelo() -> str:
    """Obtiene el modelo solicitado sin asumir una instalación local."""
    if not MODELO_OLLAMA:
        raise RuntimeError(
            "No se encontró OLLAMA_MODEL. Cree un archivo .env o configure la variable de entorno.\n"
            'PowerShell: $env:OLLAMA_MODEL="llama3.2:latest"\n'
            'Linux/macOS: export OLLAMA_MODEL="llama3.2:latest"'
        )
    return MODELO_OLLAMA


def _peticion_ollama(ruta: str, datos: dict | None = None) -> dict:
    cuerpo = json.dumps(datos).encode("utf-8") if datos is not None else None
    solicitud = Request(
        f"{URL_OLLAMA}{ruta}",
        data=cuerpo,
        headers={"Content-Type": "application/json"},
        method="POST" if datos is not None else "GET",
    )
    try:
        with urlopen(solicitud, timeout=120) as respuesta:
            return json.loads(respuesta.read().decode("utf-8"))
    except URLError as error:
        raise RuntimeError(
            "No se pudo conectar con Ollama. Ejecute Ollama y verifique "
            f"{URL_OLLAMA}. Detalle: {error.reason}"
        ) from error
    except HTTPError as error:
        detalle = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Ollama respondió HTTP {error.code}: {detalle}") from error


def verificar_modelo(modelo: str) -> None:
    """Comprueba que Ollama está activo y que el modelo solicitado existe."""
    respuesta = _peticion_ollama("/api/tags")
    disponibles = [modelo.get("name", "") for modelo in respuesta.get("models", [])]
    if modelo not in disponibles and not any(nombre.startswith(f"{modelo}:") for nombre in disponibles):
        listado = ", ".join(disponibles) or "ninguno"
        raise RuntimeError(
            f"No está instalado el modelo '{modelo}'. Modelos detectados: {listado}. "
            f"Ejecute: ollama pull {modelo}"
        )


def optimizar_guion(texto: str) -> str:
    """Convierte texto técnico en una locución clara sin alterar conceptos."""
    modelo = obtener_modelo()
    instrucciones = ARCHIVO_PROMPT.read_text(encoding="utf-8")
    prompt = (
        f"{instrucciones}\n\n"
        "Reescribe únicamente el siguiente fragmento. Devuelve solo la narración final, "
        "sin título, comillas, listas ni comentarios.\n\n"
        f"FRAGMENTO:\n{texto}"
    )
    respuesta = _peticion_ollama(
        "/api/generate",
        {
            "model": modelo,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": 0.35},
        },
    )
    resultado = respuesta.get("response", "").strip()
    if not resultado:
        raise RuntimeError("Ollama no devolvió texto para el fragmento solicitado.")
    return " ".join(resultado.split())


def main() -> int:
    try:
        verificar_modelo(obtener_modelo())
        optimizadas = [(archivo, optimizar_guion(texto)) for archivo, texto in extraer_secciones(GUION_FINAL)]
        escribir_secciones(GUION_OPTIMIZADO, optimizadas, "Guion optimizado para narración")
    except (OSError, ValueError, RuntimeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Guion optimizado creado: {GUION_OPTIMIZADO}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
