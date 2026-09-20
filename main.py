"""Escenas exportadas para Manim.

Ejemplo: manim -pqh main.py IntroduccionListasEnlazadas
"""

from escenas.introduccion import IntroduccionListasEnlazadas as _IntroduccionListasEnlazadas
from escenas.insercion import InsercionAlInicio as _InsercionAlInicio
from escenas.recorrido import RecorridoDeLista as _RecorridoDeLista
from escenas.prueba_lista_simple import PruebaListaSimple as _PruebaListaSimple
from escenas.introduccion_lista import IntroduccionLista as _IntroduccionLista
from escenas.insercion_lista import InsercionEnLista as _InsercionEnLista
from escenas.eliminacion_lista import EliminacionEnLista as _EliminacionEnLista
from escenas.referencias_lista import ReferenciasLista as _ReferenciasLista
from escenas.ventajas_lista import VentajasLista as _VentajasLista
from escenas.desventajas_lista import DesventajasLista as _DesventajasLista
from escenas.variantes_lista import VariantesLista as _VariantesLista
from escenas.aplicaciones_lista import AplicacionesLista as _AplicacionesLista
from produccion.documental import ListaEnlazadaDocumental as _ListaEnlazadaDocumental


# Manim descubre las clases declaradas en el archivo indicado por CLI. Estas
# fachadas preservan una entrada única sin duplicar la lógica de las escenas.
class IntroduccionListasEnlazadas(_IntroduccionListasEnlazadas):
    pass


class InsercionAlInicio(_InsercionAlInicio):
    pass


class RecorridoDeLista(_RecorridoDeLista):
    pass


class PruebaListaSimple(_PruebaListaSimple):
    pass


class IntroduccionLista(_IntroduccionLista):
    pass


class InsercionEnLista(_InsercionEnLista):
    pass


class EliminacionEnLista(_EliminacionEnLista):
    pass


class ReferenciasLista(_ReferenciasLista):
    pass


class VentajasLista(_VentajasLista):
    pass


class DesventajasLista(_DesventajasLista):
    pass


class VariantesLista(_VariantesLista):
    pass


class AplicacionesLista(_AplicacionesLista):
    pass


class ListaEnlazadaDocumental(_ListaEnlazadaDocumental):
    """Punto de entrada único para el render de producción."""

    pass

__all__ = [
    "IntroduccionListasEnlazadas",
    "InsercionAlInicio",
    "RecorridoDeLista",
    "PruebaListaSimple",
    "IntroduccionLista",
    "InsercionEnLista",
    "EliminacionEnLista",
    "ReferenciasLista",
    "VentajasLista",
    "DesventajasLista",
    "VariantesLista",
    "AplicacionesLista",
    "ListaEnlazadaDocumental",
]
