"""Evolución visual: lista simple, doble y circular."""

from manim import Arrow, Create, CurvedArrow, DOWN, FadeOut, GREEN, Indicate, PURPLE, Text, UP, Write

from escenas.base import EscenaListaEnlazada
from estructuras.lista_enlazada_visual import ListaEnlazadaVisual


class VariantesLista(EscenaListaEnlazada):
    def construct(self):
        self.mostrar_titulo("Evolución de las listas enlazadas")
        lista = ListaEnlazadaVisual()
        for valor in (10, 20, 30):
            lista.agregar(valor)
        lista.shift(DOWN * 0.55)

        simple = Text("Lista simplemente enlazada", font_size=29).to_edge(UP).shift(DOWN * 1.0)
        self.play(Write(simple), lista.animar_creacion_lista())
        descripcion_simple = Text("Cada nodo conoce solamente al siguiente.", font_size=24).to_edge(DOWN)
        self.play(Write(descripcion_simple))
        self.wait(0.6)
        self.play(FadeOut(simple), FadeOut(descripcion_simple))

        doble = Text("Lista doblemente enlazada", font_size=29).to_edge(UP).shift(DOWN * 1.0)
        atras_1 = Arrow(lista.nodos[1].get_top(), lista.nodos[0].get_top(), buff=0.12, color=PURPLE)
        atras_2 = Arrow(lista.nodos[2].get_top(), lista.nodos[1].get_top(), buff=0.12, color=PURPLE)
        self.play(Write(doble), Create(atras_1), Create(atras_2))
        descripcion_doble = Text("Cada nodo conoce al anterior y al siguiente.", font_size=24).to_edge(DOWN)
        ventaja = Text("+ recorrido bidireccional", font_size=23, color=GREEN).next_to(descripcion_doble, UP)
        desventaja = Text("− mayor memoria por nodo", font_size=23, color=PURPLE).next_to(descripcion_doble, DOWN)
        self.play(Write(descripcion_doble), Write(ventaja), Write(desventaja))
        self.play(Indicate(atras_1, color=PURPLE), Indicate(atras_2, color=PURPLE))
        self.play(
            FadeOut(doble), FadeOut(descripcion_doble), FadeOut(ventaja), FadeOut(desventaja),
            FadeOut(atras_1), FadeOut(atras_2),
        )

        circular = Text("Lista circular", font_size=29).to_edge(UP).shift(DOWN * 1.0)
        retorno = CurvedArrow(lista.nodos[-1].get_bottom(), lista.nodos[0].get_bottom(), angle=-3.14, color=GREEN)
        self.play(Write(circular), Create(retorno))
        explicacion = Text("El último nodo apunta nuevamente al primero.", font_size=24).to_edge(DOWN)
        self.play(Write(explicacion), Indicate(retorno, color=GREEN))
        aplicaciones = Text("Turnos  ·  Round Robin  ·  Ciclos continuos", font_size=23, color=GREEN).next_to(explicacion, UP)
        self.play(Write(aplicaciones))
        self.wait(1)
