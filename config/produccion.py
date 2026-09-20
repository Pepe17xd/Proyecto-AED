"""Configuración no visual para el render del documental."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

RAIZ_PROYECTO = Path(__file__).resolve().parent.parent
DIRECTORIO_AUDIO = RAIZ_PROYECTO / "audio"

# Las variables de la sesión tienen prioridad sobre los valores de .env.
load_dotenv(RAIZ_PROYECTO / ".env", override=False)

# La narración se habilita explícitamente en producción para que el render de
# trabajo no falle ni incorpore audio hasta que los archivos definitivos existan.
NARRACION_ACTIVA = os.getenv("MANIM_NARRACION", "0") == "1"

ARCHIVOS_NARRACION = (
    "intro.mp3",
    "referencias.mp3",
    "insercion.mp3",
    "eliminacion.mp3",
    "ventajas.mp3",
    "desventajas.mp3",
    "variantes.mp3",
    "aplicaciones.mp3",
)

# La música se mezcla en postproducción para no competir con la narración.
ARCHIVO_MUSICA_AMBIENTAL = DIRECTORIO_AUDIO / "musica_ambiental.mp3"
VOLUMEN_MUSICA = 0.12
