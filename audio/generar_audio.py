"""Genera una pista MP3 real por sección con edge-tts."""

from __future__ import annotations

import argparse
import asyncio
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

from narracion_utils import DIRECTORIO_AUDIO, GUION_FINAL, GUION_OPTIMIZADO, extraer_secciones


load_dotenv(DIRECTORIO_AUDIO.parent / ".env", override=False)
VOZ_POR_DEFECTO = os.getenv("TTS_VOICE", "es-MX-JorgeNeural")
VELOCIDAD_POR_DEFECTO = os.getenv("TTS_RATE", "-8%")
TONO_POR_DEFECTO = os.getenv("TTS_PITCH", "+0Hz")


async def sintetizar(texto: str, destino: Path, voz: str, velocidad: str, tono: str) -> None:
    """Guarda un MP3 mediante la voz neuronal elegida."""
    import edge_tts

    comunicador = edge_tts.Communicate(texto, voice=voz, rate=velocidad, pitch=tono)
    await comunicador.save(str(destino))


def argumentos() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Genera la narración MP3 por escenas.")
    parser.add_argument("--voice", default=VOZ_POR_DEFECTO, help="Voz Edge TTS, p. ej. es-MX-JorgeNeural.")
    parser.add_argument("--rate", default=VELOCIDAD_POR_DEFECTO, help="Velocidad Edge TTS, p. ej. -8%%.")
    parser.add_argument("--pitch", default=TONO_POR_DEFECTO, help="Tono Edge TTS, p. ej. +0Hz.")
    parser.add_argument("--guion", type=Path, help="Guion Markdown; por defecto prefiere el optimizado.")
    parser.add_argument("--overwrite", action="store_true", help="Reemplaza MP3 existentes.")
    return parser.parse_args()


def main() -> int:
    args = argumentos()
    guion = args.guion or (GUION_OPTIMIZADO if GUION_OPTIMIZADO.exists() else GUION_FINAL)
    try:
        import edge_tts  # noqa: F401
    except ImportError:
        print("Falta edge-tts. Instale con: python -m pip install edge-tts", file=sys.stderr)
        return 1

    try:
        for nombre, texto in extraer_secciones(guion):
            destino = DIRECTORIO_AUDIO / nombre
            if destino.exists() and not args.overwrite:
                print(f"Se conserva {nombre}; use --overwrite para regenerarlo.")
                continue
            asyncio.run(sintetizar(texto, destino, args.voice, args.rate, args.pitch))
            print(f"Generado: {destino.name}")
    except (OSError, ValueError, RuntimeError) as error:
        print(f"Error al generar audio: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
