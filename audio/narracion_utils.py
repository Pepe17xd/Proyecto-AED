"""Utilidades compartidas para el pipeline de narración."""

from __future__ import annotations

import re
from pathlib import Path


DIRECTORIO_AUDIO = Path(__file__).resolve().parent
GUION_FINAL = DIRECTORIO_AUDIO / "guion_final.md"
GUION_FINAL_V2 = DIRECTORIO_AUDIO / "guion_final_v2.md"
GUION_OPTIMIZADO = DIRECTORIO_AUDIO / "guion_optimizado.md"

PATRON_SECCION = re.compile(r"^##\s+([^\s]+\.mp3)\s+—\s+.*$", re.MULTILINE)
PATRON_ESCENA_V2 = re.compile(r"^##\s+([A-Za-z][\w]+)\s*$", re.MULTILINE)
PATRON_NARRACION_V2 = re.compile(r"\[Narraci[oó]n\]\s*\n(.+?)(?=\n\[|\Z)", re.DOTALL | re.IGNORECASE)

ARCHIVO_POR_ESCENA = {
    "IntroduccionLista": "intro.mp3",
    "ReferenciasLista": "referencias.mp3",
    "InsercionEnLista": "insercion.mp3",
    "EliminacionEnLista": "eliminacion.mp3",
    "VentajasLista": "ventajas.mp3",
    "DesventajasLista": "desventajas.mp3",
    "VariantesLista": "variantes.mp3",
    "AplicacionesLista": "aplicaciones.mp3",
}


def extraer_secciones(ruta: Path) -> list[tuple[str, str]]:
    """Extrae pares ``(archivo_mp3, texto)`` del guion Markdown."""
    contenido = ruta.read_text(encoding="utf-8")
    coincidencias = list(PATRON_SECCION.finditer(contenido))
    if not coincidencias:
        escenas = list(PATRON_ESCENA_V2.finditer(contenido))
        secciones_v2 = []
        for indice, escena in enumerate(escenas):
            fin = escenas[indice + 1].start() if indice + 1 < len(escenas) else len(contenido)
            bloque = contenido[escena.end() : fin]
            narracion = PATRON_NARRACION_V2.search(bloque)
            archivo = ARCHIVO_POR_ESCENA.get(escena.group(1))
            if archivo and narracion:
                texto = " ".join(narracion.group(1).split())
                if texto:
                    secciones_v2.append((archivo, texto))
        if secciones_v2:
            return secciones_v2
    secciones = []
    for indice, coincidencia in enumerate(coincidencias):
        fin = coincidencias[indice + 1].start() if indice + 1 < len(coincidencias) else len(contenido)
        texto = contenido[coincidencia.end() : fin].strip()
        texto = texto.removeprefix("> ").replace("\n> ", " ").strip()
        if texto:
            secciones.append((coincidencia.group(1), texto))
    if not secciones:
        raise ValueError(f"No se encontraron secciones de narración en {ruta}.")
    return secciones


def escribir_secciones(ruta: Path, secciones: list[tuple[str, str]], titulo: str) -> None:
    """Guarda las secciones en un formato consumible por el generador TTS."""
    bloques = [f"# {titulo}", ""]
    for archivo, texto in secciones:
        bloques.extend((f"## {archivo} — NARRACIÓN", "", f"> {texto}", ""))
    ruta.write_text("\n".join(bloques), encoding="utf-8")
