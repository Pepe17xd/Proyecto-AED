"""Primera escena cinematográfica: intuición de una lista enlazada simple."""

from manim import (
    Create,
    DOWN,
    FadeOut,
    GREEN,
    Indicate,
    LaggedStart,
    Rectangle,
    ReplacementTransform,
    RIGHT,
    SurroundingRectangle,
    Text,
    UP,
    VGroup,
    Write,
)

from config.estilo import COLOR_DATO, COLOR_NODO, COLOR_PUNTERO
from escenas.base import EscenaListaEnlazada
from estructuras.lista_enlazada_visual import ListaEnlazadaVisual


class IntroduccionLista(EscenaListaEnlazada):
    """Presenta el paso de datos contiguos a nodos conectados."""

    def construct(self):
        titulo = Text("Listas Enlazadas", font_size=58)
        subtitulo = Text("Conectando datos mediante referencias", font_size=28)
        subtitulo.next_to(titulo, DOWN, buff=0.35)

        self.play(Write(titulo), run_time=1.4)
        self.play(Write(subtitulo), run_time=1.1)
        self.wait(0.5)
        self.play(titulo.animate.to_edge(UP), FadeOut(subtitulo), run_time=0.8)

        arreglo = self._crear_arreglo([10, 20, 30])
        etiqueta_arreglo = Text("Datos almacenados juntos", font_size=26)
        etiqueta_arreglo.next_to(arreglo, DOWN, buff=0.55)
        self.play(LaggedStart(*[Create(celda) for celda in arreglo], lag_ratio=0.18))
        self.play(Write(etiqueta_arreglo))
        self.wait(0.5)

        # La separación abre espacio para entender que cada elemento puede
        # convertirse en una unidad que contiene dato y referencia.
        self.play(arreglo.animate.arrange(RIGHT, buff=1.15), FadeOut(etiqueta_arreglo))

        lista = ListaEnlazadaVisual()
        for valor in (10, 20, 30):
            lista.agregar(valor)
        lista.shift(DOWN * 0.55)

        primer_nodo = lista.nodos[0]
        self.play(
            ReplacementTransform(arreglo[0], primer_nodo),
            FadeOut(VGroup(arreglo[1], arreglo[2])),
            run_time=1.1,
        )

        texto_dato = Text("Cada nodo almacena un dato", font_size=27)
        texto_dato.to_edge(DOWN)
        self.play(Write(texto_dato), Indicate(primer_nodo.celda_dato, color=COLOR_NODO))
        self.wait(0.35)

        texto_referencia = Text("y una referencia al siguiente nodo", font_size=27)
        texto_referencia.move_to(texto_dato)
        self.play(
            ReplacementTransform(texto_dato, texto_referencia),
            Indicate(primer_nodo.celda_puntero, color=COLOR_PUNTERO),
        )

        # Los nodos y flechas pertenecen a ListaEnlazadaVisual; solo se
        # orquesta su orden de aparición para contar la idea paso a paso.
        self.play(lista.nodos[1].animar_creacion())
        self.play(Create(lista.enlaces[0]))
        self.play(lista.nodos[2].animar_creacion())
        self.play(Create(lista.enlaces[1]))
        self.play(FadeOut(texto_referencia))

        marco = SurroundingRectangle(lista, color=GREEN, buff=0.28, corner_radius=0.12)
        self.play(Create(marco), Indicate(lista, color=GREEN, scale_factor=1.04))
        self.wait(1.2)

    @staticmethod
    def _crear_arreglo(valores):
        """Construye una representación compacta de un arreglo contiguo."""
        celdas = VGroup()
        for valor in valores:
            marco = Rectangle(width=1.25, height=0.78, color=COLOR_NODO)
            dato = Text(str(valor), font_size=30, color=COLOR_DATO).move_to(marco)
            celdas.add(VGroup(marco, dato))
        return celdas.arrange(RIGHT, buff=0)
