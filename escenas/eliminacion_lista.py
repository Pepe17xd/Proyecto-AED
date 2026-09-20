"""Escena didáctica: eliminación de un nodo en una lista enlazada simple."""

from manim import Create, DOWN, FadeOut, GREEN, Indicate, RED, SurroundingRectangle, Text, UP, Write

from escenas.base import EscenaListaEnlazada
from estructuras.lista_enlazada_visual import ListaEnlazadaVisual


class EliminacionEnLista(EscenaListaEnlazada):
    """Elimina 20 y muestra la reconexión directa de 15 con 30."""

    def construct(self):
        self.mostrar_titulo("Eliminación en una lista enlazada")
        lista = ListaEnlazadaVisual()
        for valor in (10, 15, 20, 30):
            lista.agregar(valor)
        lista.shift(DOWN * 0.45)

        self.play(lista.animar_creacion_lista())
        self.wait(0.4)

        objetivo = Text("Eliminar nodo 20", font_size=28, color=RED).to_edge(UP)
        objetivo.shift(DOWN * 1.05)
        nodo_eliminado = lista.nodos[2]
        self.play(Write(objetivo), Indicate(nodo_eliminado, color=RED, scale_factor=1.12))

        # Se enfatiza el tramo cuya referencia será reescrita antes de usar la
        # operación existente de la estructura para efectuar el cambio.
        explicacion = Text("La referencia de 15 debe apuntar a 30", font_size=25)
        explicacion.to_edge(DOWN)
        self.play(
            Write(explicacion),
            Indicate(lista.nodos[1], color=GREEN),
            Indicate(lista.enlaces[1], color=RED),
            Indicate(lista.enlaces[2], color=RED),
        )

        self.play(lista.eliminar(3))
        self.play(FadeOut(objetivo), FadeOut(explicacion))

        resultado = Text("10  →  15  →  30", font_size=28, color=GREEN).to_edge(DOWN)
        marco = SurroundingRectangle(lista, color=GREEN, buff=0.25, corner_radius=0.1)
        self.play(Write(resultado), Create(marco), Indicate(lista, color=GREEN))
        self.wait(1)
