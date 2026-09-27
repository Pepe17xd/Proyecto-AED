"""Mezcla un documental ya narrado con música ambiental usando FFmpeg."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


RAIZ_PROYECTO = Path(__file__).resolve().parent.parent
VIDEO_POR_DEFECTO = RAIZ_PROYECTO / "media" / "videos" / "main" / "1080p60" / "ListaEnlazadaDocumental.mp4"
MUSICA_POR_DEFECTO = RAIZ_PROYECTO / "audio" / "musica_ambiental.mp3"
SALIDA_POR_DEFECTO = RAIZ_PROYECTO / "video_final_listas_enlazadas.mp4"


def argumentos() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Mezcla voz del documental con música ambiental.")
    parser.add_argument("--video", type=Path, default=VIDEO_POR_DEFECTO, help="MP4 narrado de Manim.")
    parser.add_argument("--musica", type=Path, default=MUSICA_POR_DEFECTO, help="Pista instrumental MP3.")
    parser.add_argument("--salida", type=Path, default=SALIDA_POR_DEFECTO, help="MP4 final.")
    parser.add_argument("--volumen-musica", type=float, default=0.12, help="Entre 0.10 y 0.15; por defecto 0.12.")
    return parser.parse_args()


def main() -> int:
    args = argumentos()
    if not shutil.which("ffmpeg"):
        print("No se encontró FFmpeg en PATH.", file=sys.stderr)
        return 1
    if not args.video.is_file():
        print(f"No existe el vídeo narrado: {args.video}", file=sys.stderr)
        return 1
    if not args.musica.is_file():
        print(f"No existe la música ambiental: {args.musica}", file=sys.stderr)
        return 1
    if not 0.10 <= args.volumen_musica <= 0.15:
        print("El volumen de música debe estar entre 0.10 y 0.15.", file=sys.stderr)
        return 1

    filtro = (
        f"[1:a]volume={args.volumen_musica}[musica];"
        "[0:a][musica]amix=inputs=2:duration=first:normalize=0[a]"
    )
    comando = [
        "ffmpeg", "-y", "-i", str(args.video), "-stream_loop", "-1", "-i", str(args.musica),
        "-filter_complex", filtro, "-map", "0:v:0", "-map", "[a]", "-c:v", "copy", "-c:a", "aac",
        "-shortest", str(args.salida),
    ]
    try:
        subprocess.run(comando, check=True)
    except subprocess.CalledProcessError as error:
        print(f"FFmpeg no pudo generar la mezcla (código {error.returncode}).", file=sys.stderr)
        return error.returncode
    print(f"Vídeo final creado: {args.salida}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
