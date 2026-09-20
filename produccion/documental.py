"""Escena orquestadora que une las secciones del documental."""

from __future__ import annotations

from types import MethodType

from manim import FadeOut, Group

from config.produccion import DIRECTORIO_AUDIO, NARRACION_ACTIVA
from escenas.aplicaciones_lista import AplicacionesLista
from escenas.base import EscenaListaEnlazada
from escenas.cierre_documental import CierreDocumental
from escenas.creditos_documental import CreditosDocumental
from escenas.desventajas_lista import DesventajasLista
from escenas.eliminacion_lista import EliminacionEnLista
from escenas.insercion_lista import InsercionEnLista
from escenas.introduccion_lista import IntroduccionLista
from escenas.referencias_lista import ReferenciasLista
from escenas.variantes_lista import VariantesLista
from escenas.ventajas_lista import VentajasLista


class ListaEnlazadaDocumental(EscenaListaEnlazada):
    """Renderiza el relato completo en un único archivo de vídeo.

    Las escenas existentes se ejecutan sobre el mismo lienzo. Entre secciones
    se elimina el estado visual con un fundido breve, sin cambiar su lógica.
    """

    SECCIONES = (
        (IntroduccionLista, "intro.mp3"),
        (ReferenciasLista, "referencias.mp3"),
        (InsercionEnLista, "insercion.mp3"),
        (EliminacionEnLista, "eliminacion.mp3"),
        (VentajasLista, "ventajas.mp3"),
        (DesventajasLista, "desventajas.mp3"),
        (VariantesLista, "variantes.mp3"),
        (AplicacionesLista, "aplicaciones.mp3"),
    )

    def construct(self):

        if NARRACION_ACTIVA:
            self.add_sound(
                str(DIRECTORIO_AUDIO / "narracion_completa.mp3")
            )

        CreditosDocumental.construct(self)
        self._transicion()

        for escena, archivo_audio in self.SECCIONES:
            self._ejecutar_escena(escena)
            self._transicion()

        CierreDocumental.construct(self)

    def _agregar_narracion(self, nombre_archivo: str) -> None:
            ruta = DIRECTORIO_AUDIO / nombre_archivo
            print("Audio:", ruta)
            print("Existe:", ruta.exists())
            print("Narración activa:", NARRACION_ACTIVA)

            if NARRACION_ACTIVA and ruta.is_file():
                self.add_sound(str(ruta))

    def _transicion(self) -> None:
        """Fundido suave y limpieza explícita entre dos escenas independientes."""
        if self.mobjects:
            self.play(FadeOut(Group(*self.mobjects)), run_time=0.55)
        self.clear()
        self.wait(0.15)

    def _ejecutar_escena(self, clase_escena) -> None:
        """Ejecuta una escena existente conservando sus auxiliares privados.

        Las escenas se mantienen independientes y algunas declaran helpers
        estáticos para construir arreglos o listas. Se montan solo durante esa
        sección sobre esta instancia de producción y luego se restauran.
        """
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
                setattr(self, nombre, descriptor.__get__(clase_escena, clase_escena))
            elif callable(descriptor):
                setattr(self, nombre, MethodType(descriptor, self))

        try:
            clase_escena.construct(self)
        finally:
            for nombre, existia, anterior in reversed(restauraciones):
                if existia:
                    setattr(self, nombre, anterior)
                else:
                    delattr(self, nombre)
