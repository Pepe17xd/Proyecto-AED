"""Cierre visual del documental."""

from manim import DOWN, FadeOut, GREEN, Text, VGroup, Write

from escenas.base import EscenaListaEnlazada


class CierreDocumental(EscenaListaEnlazada):
    """Cierra la narrativa con la idea central de las referencias."""

    def construct(self):
        primera_idea = Text("Las listas enlazadas no almacenan datos juntos...", font_size=34)
        segunda_idea = Text("...los conectan mediante referencias.", font_size=36, color=GREEN)
        segunda_idea.next_to(primera_idea, DOWN, buff=0.45)

        self.play(Write(primera_idea), run_time=1.2)
        self.wait(1.0)
        self.play(Write(segunda_idea), run_time=1.1)
        self.wait(1.3)
        self.play(FadeOut(primera_idea), FadeOut(segunda_idea), run_time=0.6)

        realizado_por = Text("Proyecto realizado por", font_size=27, color=GREEN)
        nombres = VGroup(
            Text("Antony Yonel Rosales Esteban", font_size=27),
            Text("Jeseph Imanol Burgos Ochoa", font_size=27),
        ).arrange(DOWN, buff=0.2)
        curso = Text("Algoritmos y Estructuras de Datos", font_size=24)
        creditos = VGroup(realizado_por, nombres, curso).arrange(DOWN, buff=0.42)

        self.play(Write(realizado_por), run_time=0.7)
        self.play(Write(nombres), run_time=0.9)
        self.play(Write(curso), run_time=0.7)
        self.wait(1.6)
        self.play(FadeOut(creditos), run_time=0.9)
