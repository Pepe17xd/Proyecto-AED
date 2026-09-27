"""Explica que una lista enlazada cambia conexiones, no datos."""

from manim import Create, DOWN, FadeOut, GREEN, Indicate, SurroundingRectangle, Text, TransformFromCopy, UP, Write

from componentes.nodo_visual import NodoVisual
from escenas.base import EscenaListaEnlazada
from estructuras.lista_enlazada_visual import ListaEnlazadaVisual


class ReferenciasLista(EscenaListaEnlazada):
    def construct(self):
        self.mostrar_titulo("El secreto está en las referencias")
        lista = ListaEnlazadaVisual()
        for valor in (10, 20, 30):
            lista.agregar(valor)
        lista.shift(DOWN * 0.7)
        self.play(lista.animar_creacion_lista())

        foco = NodoVisual(20).scale(1.45).move_to(DOWN * 0.35)
        etiqueta = Text("Un nodo", font_size=28).next_to(foco, UP)
        self.play(
            FadeOut(lista.nodos[0]), FadeOut(lista.nodos[2]), FadeOut(lista.enlaces),
            TransformFromCopy(lista.nodos[1], foco), Write(etiqueta),
        )
        self.play(Indicate(foco.celda_dato, color=GREEN))
        dato = Text("El dato almacena información", font_size=25).to_edge(DOWN)
        self.play(Write(dato))
        referencia = Text("La referencia indica hacia dónde apunta", font_size=25).move_to(dato)
        self.play(FadeOut(dato), Write(referencia), Indicate(foco.celda_puntero, color=GREEN))
        self.play(FadeOut(foco), FadeOut(etiqueta), FadeOut(referencia))

        # La estructura existente realiza el cambio real de referencias.
        self.play(*[nodo.animate.set_opacity(1) for nodo in lista.nodos], Create(lista.enlaces))
        antes = Text("Antes: 10.next = 20", font_size=26).to_edge(UP).shift(DOWN * 1.0)
        self.play(Write(antes), Indicate(lista.enlaces[0], color=GREEN))
        self.play(lista.insertar(15, 2))
        despues = Text("Después: 10.next = 15   ·   15.next = 20", font_size=25).move_to(antes)
        self.play(FadeOut(antes), Write(despues))
        conclusion = Text("No se reorganizan datos: se modifican conexiones.", font_size=26, color=GREEN).to_edge(DOWN)
        self.play(Write(conclusion), Indicate(lista, color=GREEN))
        self.wait(1)
