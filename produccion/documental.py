"""Escena orquestadora que une las secciones del documental."""

from __future__ import annotations

from types import MethodType

from manim import FadeOut, Group, config

from config.produccion import DIRECTORIO_AUDIO, NARRACION_ACTIVA
from escenas.aplicaciones_lista import AplicacionesLista
from escenas.base import EscenaListaEnlazada
from escenas.cierre_documental import CierreDocumental
from escenas.creditos_documental import CreditosDocumental
from escenas.desventajas_lista import DesventajasLista
from escenas.eliminacion_lista import EliminacionEnLista
from escenas.insercion_lista import InsercionEnLista
from escenas.introduccion_lista import IntroduccionLista
from escenas.introduccion_concepto import IntroduccionConcepto
from escenas.referencias_lista import ReferenciasLista
from escenas.variantes_lista import VariantesLista
from escenas.ventajas_lista import VentajasLista


class ListaEnlazadaDocumental(EscenaListaEnlazada):
    """Renderiza el relato completo en un único archivo de vídeo.

    Las escenas existentes se ejecutan sobre el mismo lienzo. Entre secciones
    se elimina el estado visual con un fundido breve, sin cambiar su lógica.
    """

    SECCIONES = (
        (IntroduccionConcepto, "concepto.mp3"),
        (IntroduccionLista, "intro.mp3"),
        (ReferenciasLista, "referencias.mp3"),
        (InsercionEnLista, "insercion.mp3"),
        (EliminacionEnLista, "eliminacion.mp3"),
        (VentajasLista, "ventajas.mp3"),
        (DesventajasLista, "desventajas.mp3"),
        (VariantesLista, "variantes.mp3"),
        (AplicacionesLista, "aplicaciones.mp3"),
    )

    def setup(self):
        """Prepara una línea de tiempo reproducible cuando hay narración.

        ``Scene.add_sound`` no registra sonido mientras el renderer reutiliza
        una animación desde caché. Como cada pista depende del instante actual
        de esta escena, un render narrado debe ejecutar todas las animaciones
        y no puede reutilizar fragmentos de vídeo.
        """
        if NARRACION_ACTIVA:
            config.disable_caching = True
        super().setup()

    def construct(self):

        CreditosDocumental.construct(self)

        self._transicion()

        for escena, archivo_audio in self.SECCIONES:
            self._ejecutar_escena(
                escena,
                archivo_audio
            )

            self._transicion()

        CierreDocumental.construct(self)

    def _agregar_narracion(self, nombre_archivo: str) -> None:
        """Inserta la pista de su escena en el instante visual actual."""
        ruta = DIRECTORIO_AUDIO / nombre_archivo
        if NARRACION_ACTIVA and ruta.is_file():
            self.add_sound(str(ruta))

    def _transicion(self) -> None:
        """Fundido suave y limpieza explícita entre dos escenas independientes."""
        if self.mobjects:
            self.play(FadeOut(Group(*self.mobjects)), run_time=0.55)
        self.clear()
        self.wait(0.15)

    def _ejecutar_escena(self, clase_escena, archivo_audio: str) -> None:
        """Ejecuta una sección con su narración sincronizada."""

        restauraciones = []

        for nombre, descriptor in vars(clase_escena).items():
            if not nombre.startswith("_") or nombre.startswith("__"):
                continue

            anterior = getattr(self, nombre, None)
            existia = hasattr(self, nombre)

            restauraciones.append((nombre, existia, anterior))

            if isinstance(descriptor, staticmethod):
                setattr(self, nombre, descriptor.__func__)

            elif isinstance(descriptor, classmethod):
                setattr(
                    self,
                    nombre,
                    descriptor.__get__(clase_escena, clase_escena)
                )

            elif callable(descriptor):
                setattr(
                    self,
                    nombre,
                    MethodType(descriptor, self)
                )

        try:
            inicio_narracion = self.time
            self._agregar_narracion(archivo_audio)

            clase_escena.construct(self)

            # Mantiene el último plano únicamente el tiempo que falte para
            # terminar la pista; no introduce un porcentaje arbitrario ni
            # desplaza el inicio de la siguiente sección.
            duracion_audio = self._duracion_audio(
                DIRECTORIO_AUDIO / archivo_audio
            )
            restante = max(0.0, duracion_audio - (self.time - inicio_narracion))
            if restante:
                self.wait(restante)

        finally:
            for nombre, existia, anterior in reversed(restauraciones):
                if existia:
                    setattr(self, nombre, anterior)
                else:
                    delattr(self, nombre)

    @staticmethod
    def _duracion_audio(ruta) -> float:
        """Lee duración MP3 con PyAV, incluido con Manim, sin depender de ffprobe."""
        if not ruta.is_file():
            return 0.0
        try:
            import av
            with av.open(str(ruta)) as contenedor:
                return float(contenedor.duration / av.time_base) if contenedor.duration else 0.0
        except (OSError, ImportError, ValueError):
            return 0.0
