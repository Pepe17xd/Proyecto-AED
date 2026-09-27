"""Apertura visual del documental."""

from manim import DOWN, FadeOut, GREEN, Text, VGroup, Write

from escenas.base import EscenaListaEnlazada


class CreditosDocumental(EscenaListaEnlazada):
    """Créditos iniciales de bajo ruido visual."""

    def construct(self):
        titulo = Text("Animando Estructuras de Datos", font_size=52)
        subtitulo = Text("Listas Enlazadas", font_size=34, color=GREEN)
        subtitulo.next_to(titulo, DOWN, buff=0.35)
        proyecto = Text("Proyecto de animación educativa", font_size=22)
        proyecto.next_to(subtitulo, DOWN, buff=0.65)

        autoria = Text("Integrantes", font_size=23, color=GREEN)
        nombres = VGroup(
            Text("Antony Yonel Rosales Esteban", font_size=25),
            Text("Jeseph Imanol Burgos Ochoa", font_size=25),
        ).arrange(DOWN, buff=0.18)
        creditos = VGroup(autoria, nombres).arrange(DOWN, buff=0.3).to_edge(DOWN)

        self.play(Write(titulo), run_time=1.4)
        self.play(Write(subtitulo), run_time=0.9)
        self.play(Write(proyecto), run_time=0.6)
        self.play(Write(autoria), Write(nombres), run_time=0.9)
        self.wait(1.2)
        self.play(FadeOut(VGroup(titulo, subtitulo, proyecto, creditos)), run_time=0.8)
