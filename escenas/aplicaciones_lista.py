"""Aplicaciones cotidianas de listas dobles y circulares."""

from manim import Arrow, Create, CurvedArrow, DOWN, DoubleArrow, GREEN, LEFT, RIGHT, Text, UP, VGroup, Write

from escenas.base import EscenaListaEnlazada
from estructuras.lista_enlazada_visual import ListaEnlazadaVisual


class AplicacionesLista(EscenaListaEnlazada):
    def construct(self):
        self.mostrar_titulo("Aplicaciones reales")

        navegador = self._cadena(("Anterior", "Página actual", "Siguiente")).shift(UP * 1.65)
        self.play(Write(Text("Navegador", font_size=27).next_to(navegador, UP)), Create(navegador))

        musica = self._cadena(("Canción anterior", "Actual", "Próxima")).shift(DOWN * 0.1)
        self.play(Write(Text("Reproductor musical", font_size=27).next_to(musica, UP)), Create(musica))

        turnos = ListaEnlazadaVisual()
        for jugador in ("Jugador 1", "Jugador 2", "Jugador 3"):
            turnos.agregar(jugador)
        turnos.shift(DOWN * 1.75)
        retorno = CurvedArrow(turnos.nodos[-1].get_bottom(), turnos.nodos[0].get_bottom(), angle=-3.14, color=GREEN)
        self.play(Write(Text("Sistemas de turnos", font_size=27).next_to(turnos, UP)), turnos.animar_creacion_lista())
        self.play(Create(retorno))
        self.wait(1)

    @staticmethod
    def _cadena(etiquetas):
        elementos = VGroup(*[Text(etiqueta, font_size=23) for etiqueta in etiquetas]).arrange(RIGHT, buff=1.05)
        flechas = VGroup(
            DoubleArrow(elementos[0].get_right(), elementos[1].get_left(), buff=0.18),
            DoubleArrow(elementos[1].get_right(), elementos[2].get_left(), buff=0.18),
        )
        return VGroup(elementos, flechas)
