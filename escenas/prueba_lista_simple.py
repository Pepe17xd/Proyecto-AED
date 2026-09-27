"""Escena de integración para la lista enlazada visual."""

from manim import DOWN, Text

from escenas.base import EscenaListaEnlazada
from estructuras.lista_enlazada_visual import ListaEnlazadaVisual


class PruebaListaSimple(EscenaListaEnlazada):
    """Muestra creación, inserción y eliminación paso a paso."""

    def construct(self):
        titulo = self.mostrar_titulo("Lista Enlazada Simple")
        lista = ListaEnlazadaVisual()
        for valor in (10, 20, 30):
            lista.agregar(valor)
        lista.shift(DOWN * 0.4)

        self.play(lista.animar_creacion_lista())
        self.wait(0.5)
        self.play(lista.insertar(15, 2))
        self.wait(0.5)
        self.play(lista.eliminar(3))  # El 20 pasa a ocupar la tercera posición.
        self.wait(1)
