"""Componentes de alto nivel para listas enlazadas."""

from manim import Arrow, RIGHT, UP, Text, VGroup

from componentes.nodo import NodoLista
from config.estilo import COLOR_NULL, COLOR_PUNTERO, ESPACIO_NODOS


class ListaEnlazadaVisual(VGroup):
    """Lista con nodos, enlaces y etiqueta `head`.

    Las escenas usan esta interfaz, sin calcular flechas ni posiciones.
    """

    def __init__(self, valores, mostrar_null=True, **kwargs):
        super().__init__(**kwargs)
        self.nodos = [NodoLista(valor) for valor in valores]
        self.enlaces = VGroup()
        self.cabeza = Text("head", font_size=24, color=COLOR_PUNTERO)
        self.nulo = None
        for anterior, actual in zip(self.nodos, self.nodos[1:]):
            actual.next_to(anterior, RIGHT, buff=ESPACIO_NODOS)
            self.enlaces.add(self._flecha(anterior.puerto_salida, actual.get_left()))
        if self.nodos:
            self.cabeza.next_to(self.nodos[0], UP, buff=0.35)
            if mostrar_null:
                self.nulo = Text("None", font_size=26, color=COLOR_NULL)
                self.nulo.next_to(self.nodos[-1], RIGHT, buff=ESPACIO_NODOS)
                self.enlaces.add(self._flecha(self.nodos[-1].puerto_salida, self.nulo.get_left()))
        self.add(*self.nodos, self.enlaces)
        if self.nodos:
            self.add(self.cabeza)
        if self.nulo:
            self.add(self.nulo)

    def _flecha(self, inicio, fin):
        return Arrow(inicio, fin, buff=0.08, color=COLOR_PUNTERO, stroke_width=4)

    def enlace_entre(self, indice_origen, indice_destino):
        return self._flecha(self.nodos[indice_origen].puerto_salida, self.nodos[indice_destino].get_left())
