"""Base común para escenas."""

from manim import FadeOut, Scene, Text, UP, Write


class EscenaListaEnlazada(Scene):
    def mostrar_titulo(self, texto):
        titulo = Text(texto, font_size=40).to_edge(UP)
        self.play(Write(titulo))
        return titulo

    def limpiar(self, *mobjects):
        self.play(*[FadeOut(mob) for mob in mobjects])
