"""Introducción conceptual: del almacenamiento aislado a la conexión."""

from manim import (
    BLUE_E,
    DOWN,
    FadeIn,
    FadeOut,
    GREEN_C,
    GrowArrow,
    LEFT,
    ORANGE,
    RIGHT,
    RoundedRectangle,
    Text,
    UP,
    VGroup,
    WHITE,
    Write,
    Arrow,
)

from config.estilo import COLOR_DATO, COLOR_NODO, COLOR_PUNTERO
from escenas.base import EscenaListaEnlazada


class IntroduccionConcepto(EscenaListaEnlazada):
    """Plantea el problema antes de presentar una lista enlazada."""

    def construct(self):
        titulo = Text("Listas Enlazadas", font_size=52)
        subtitulo = Text(
            "Comprendiendo cómo los datos se conectan en memoria",
            font_size=25,
            color=COLOR_PUNTERO,
        )
        subtitulo.next_to(titulo, DOWN, buff=0.3)
        indice = VGroup(
            Text("1  Concepto", font_size=24, color=GREEN_C),
            Text("2  Estructura del nodo", font_size=24),
            Text("3  Inserción", font_size=24),
            Text("4  Eliminación", font_size=24),
            Text("5  Ventajas y desventajas", font_size=24),
            Text("6  Variantes", font_size=24),
            Text("7  Aplicaciones", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).scale(0.8)
        indice.next_to(subtitulo, DOWN, buff=0.55)

        self.play(Write(titulo), run_time=0.9)
        self.play(FadeIn(subtitulo, shift=UP * 0.15), run_time=0.6)
        self.play(FadeIn(indice, shift=UP * 0.2), run_time=0.8)
        self.wait(1.4)
        self.play(FadeOut(VGroup(titulo, subtitulo, indice)), run_time=0.55)

        pregunta = Text("¿Por qué necesitamos listas enlazadas?", font_size=38)
        self.play(Write(pregunta), run_time=0.9)
        self.wait(0.65)
        self.play(FadeOut(pregunta), run_time=0.4)

        datos = self._crear_datos((10, 20, 30, 40))
        etiqueta = Text("Datos almacenados como elementos contiguos", font_size=25)
        etiqueta.to_edge(DOWN)
        self.play(FadeIn(datos, shift=UP * 0.2, lag_ratio=0.12), run_time=1.2)
        self.play(Write(etiqueta), run_time=0.55)
        self.wait(0.7)

        limitacion = Text(
            "Insertar o reorganizar puede exigir mover muchos elementos",
            font_size=26,
            color=ORANGE,
        )
        limitacion.to_edge(DOWN)
        self.play(FadeOut(etiqueta), Write(limitacion), run_time=0.85)
        self.play(
            *[dato.animate.set_stroke(color=ORANGE, width=3) for dato in datos],
            run_time=0.65,
        )
        self.wait(0.7)

        aislados = self._crear_datos((10, 20, 30))
        aislados.move_to(datos)
        self.play(FadeOut(datos), FadeOut(limitacion), run_time=0.45)
        self.play(FadeIn(aislados, shift=UP * 0.15, lag_ratio=0.12), run_time=0.9)

        nodos = self._crear_nodos((10, 20, 30))
        nodos.move_to(aislados)
        flechas = VGroup(
            Arrow(nodos[0].get_right(), nodos[1].get_left(), buff=0.12, color=COLOR_PUNTERO),
            Arrow(nodos[1].get_right(), nodos[2].get_left(), buff=0.12, color=COLOR_PUNTERO),
        )
        nulo = Text("null", font_size=22, color=WHITE).next_to(nodos[2], RIGHT, buff=0.25)
        self.play(FadeOut(aislados), FadeIn(nodos, scale=0.86), run_time=0.75)
        self.play(GrowArrow(flechas[0]), GrowArrow(flechas[1]), run_time=0.8)
        self.play(FadeIn(nulo, shift=RIGHT * 0.15), run_time=0.45)
        self.wait(0.7)

        explicacion = Text(
            "Cada nodo guarda un dato y una referencia al siguiente",
            font_size=27,
            color=GREEN_C,
        ).to_edge(DOWN)
        self.play(Write(explicacion), run_time=0.85)
        self.play(
            nodos[0][1].animate.set_color(COLOR_DATO),
            nodos[0][2].animate.set_color(COLOR_PUNTERO),
            run_time=0.5,
        )
        self.wait(1.0)
        cierre = Text("Ahora podemos recorrer la cadena, nodo a nodo.", font_size=28)
        cierre.next_to(explicacion, UP, buff=0.25)
        self.play(Write(cierre), run_time=0.75)
        self.wait(11.2)
        self.play(FadeOut(VGroup(nodos, flechas, nulo, explicacion, cierre)), run_time=0.55)

    @staticmethod
    def _crear_datos(valores):
        celdas = VGroup()
        for valor in valores:
            caja = RoundedRectangle(width=1.35, height=0.82, corner_radius=0.12, color=COLOR_NODO)
            texto = Text(str(valor), font_size=29, color=COLOR_DATO).move_to(caja)
            celdas.add(VGroup(caja, texto))
        return celdas.arrange(RIGHT, buff=0.18)

    @staticmethod
    def _crear_nodos(valores):
        nodos = VGroup()
        for valor in valores:
            caja = RoundedRectangle(width=2.05, height=0.9, corner_radius=0.12, color=BLUE_E)
            dato = Text(str(valor), font_size=27, color=COLOR_DATO).move_to(caja.get_left() + RIGHT * 0.45)
            separador = Text("|", font_size=25, color=WHITE).move_to(caja.get_center())
            referencia = Text("next", font_size=20, color=COLOR_PUNTERO).move_to(caja.get_right() + LEFT * 0.4)
            nodos.add(VGroup(caja, dato, separador, referencia))
        return nodos.arrange(RIGHT, buff=0.72)
