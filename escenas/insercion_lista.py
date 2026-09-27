"""Escena didáctica: inserción animada en una lista simplemente enlazada."""

from manim import Create, DOWN, FadeOut, GREEN, Indicate, SurroundingRectangle, Text, UP, Write

from escenas.base import EscenaListaEnlazada
from config.estilo import COLOR_NODO_NUEVO
from estructuras.lista_enlazada_visual import ListaEnlazadaVisual


class InsercionEnLista(EscenaListaEnlazada):
    """Inserta 15 entre 10 y 20 mediante la API de la estructura visual."""

    def construct(self):
        titulo = self.mostrar_titulo("Inserción en una lista enlazada")
        lista = ListaEnlazadaVisual()
        for valor in (10, 20, 30):
            lista.agregar(valor)
        lista.shift(DOWN * 0.45)

        self.play(lista.animar_creacion_lista())
        self.wait(0.4)

        instruccion = Text("Insertar 15 en la posición 2", font_size=28).to_edge(UP)
        instruccion.shift(DOWN * 1.05)
        self.play(Write(instruccion), Indicate(lista.nodos[0], color=GREEN))

        # `insertar` crea el nodo, sustituye 10 → 20 por 10 → 15 → 20
        # y redistribuye la lista de forma automática.
        animacion_insercion = lista.insertar(15, 2)
        # El nodo ya existe lógicamente antes de reproducir la animación.
        lista.nodos[1].set_stroke(COLOR_NODO_NUEVO)
        self.play(animacion_insercion)
        self.play(FadeOut(instruccion))

        resultado = Text("10  →  15  →  20  →  30", font_size=28, color=GREEN)
        resultado.to_edge(DOWN)
        marco = SurroundingRectangle(lista, color=GREEN, buff=0.25, corner_radius=0.1)
        self.play(Write(resultado), Create(marco), Indicate(lista, color=GREEN))
        self.wait(1)
