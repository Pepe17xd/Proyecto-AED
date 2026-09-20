"""Escena 2: inserción al inicio."""

from manim import Create, FadeIn, Indicate, LEFT, Text, UP

from componentes.lista_enlazada import ListaEnlazadaVisual
from componentes.nodo import NodoLista
from config.estilo import COLOR_RESALTADO
from escenas.base import EscenaListaEnlazada


class InsercionAlInicio(EscenaListaEnlazada):
    def construct(self):
        self.mostrar_titulo("Inserción al inicio")
        lista = ListaEnlazadaVisual([20, 30]).move_to((0.7, -0.5, 0))
        nuevo = NodoLista(10).next_to(lista.nodos[0], LEFT, buff=0.9)
        explicacion = Text("1. nuevo.next = head", font_size=26).to_edge(UP).shift((0, -1.1, 0))
        self.play(Create(lista))
        self.play(FadeIn(nuevo), FadeIn(explicacion))
        enlace_nuevo = lista._flecha(nuevo.puerto_salida, lista.nodos[0].get_left())
        self.play(Create(enlace_nuevo), Indicate(nuevo, color=COLOR_RESALTADO))
        self.wait(1)
