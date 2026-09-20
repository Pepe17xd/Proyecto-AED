"""Base común para escenas."""

from manim import FadeOut, Scene, Text, UP, Write

from config.estilo import FONDO_CINEMATICO


class EscenaListaEnlazada(Scene):
    def setup(self):
        """Aplica un fondo uniforme sin alterar las estructuras visuales."""
        super().setup()
        self.camera.background_color = FONDO_CINEMATICO

    def mostrar_titulo(self, texto):
        titulo = Text(texto, font_size=40).to_edge(UP)
        self.play(Write(titulo))
        return titulo

    def limpiar(self, *mobjects):
        self.play(*[FadeOut(mob) for mob in mobjects])
