"""Escena 3: recorrido secuencial."""

from manim import Create, Indicate

from componentes.lista_enlazada import ListaEnlazadaVisual
from config.estilo import COLOR_RESALTADO
from escenas.base import EscenaListaEnlazada


class RecorridoDeLista(EscenaListaEnlazada):
    def construct(self):
        self.mostrar_titulo("Recorrido de la lista")
        lista = ListaEnlazadaVisual([4, 8, 15, 16]).move_to((0, -0.5, 0))
        self.play(Create(lista))
        for nodo in lista.nodos:
            self.play(Indicate(nodo, color=COLOR_RESALTADO))
        self.wait(1)
