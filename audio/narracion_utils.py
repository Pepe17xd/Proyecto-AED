"""Utilidades compartidas para el pipeline de narración."""

from __future__ import annotations

import re
from pathlib import Path


DIRECTORIO_AUDIO = Path(__file__).resolve().parent
GUION_FINAL = DIRECTORIO_AUDIO / "guion_final.md"
GUION_OPTIMIZADO = DIRECTORIO_AUDIO / "guion_optimizado.md"

PATRON_SECCION = re.compile(r"^##\s+([^\s]+\.mp3)\s+—\s+.*$", re.MULTILINE)


def extraer_secciones(ruta: Path) -> list[tuple[str, str]]:
    """Extrae pares ``(archivo_mp3, texto)`` del guion Markdown."""
    contenido = ruta.read_text(encoding="utf-8")
    coincidencias = list(PATRON_SECCION.finditer(contenido))
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
