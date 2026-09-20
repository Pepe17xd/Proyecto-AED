"""Escena 1: concepto de lista enlazada."""

from manim import Create, FadeIn, DOWN, Text

from componentes.lista_enlazada import ListaEnlazadaVisual
from escenas.base import EscenaListaEnlazada


class IntroduccionListasEnlazadas(EscenaListaEnlazada):
    def construct(self):
        titulo = self.mostrar_titulo("Listas enlazadas")
        definicion = Text("Cada nodo guarda un dato y un enlace al siguiente.", font_size=28)
        definicion.next_to(titulo, DOWN, buff=0.5)
        lista = ListaEnlazadaVisual([10, 25, 42]).move_to((0, -0.7, 0))
        self.play(FadeIn(definicion))
        self.play(*[nodo.animar_creacion() for nodo in lista.nodos])
        self.play(Create(lista.enlaces), FadeIn(lista.cabeza), FadeIn(lista.nulo))
        self.wait(1)
