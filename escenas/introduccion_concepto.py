"""Introducción conceptual: el costo de insertar y la solución con referencias.

El ritmo de esta escena está calibrado para acompañar la narración
(~40-43 s). Cada bloque de animación reparte su tiempo interno para que la
imagen avance al mismo paso que la frase correspondiente del guion, en vez
de terminar antes y dejar al espectador esperando en un plano fijo mientras
el narrador sigue hablando.
"""

from manim import (
    BLUE_E,
    DOWN,
    FadeIn,
    FadeOut,
    GREEN_C,
    GrowArrow,
    Indicate,
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
    """Plantea el problema de los arreglos y presenta la solución: nodos y referencias."""

    def construct(self):
        self._mostrar_titulo_indice()
        self._mostrar_problema_arreglo()
        nodos, flechas = self._mostrar_solucion_lista()
        self._cerrar_concepto(nodos, flechas)

    # ------------------------------------------------------------------
    # 1. Portada e índice · ~4.4 s → frase 1 del guion (~4.0 s)
    # ------------------------------------------------------------------
    def _mostrar_titulo_indice(self):
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

        self.play(Write(titulo), run_time=1.0)
        self.play(FadeIn(subtitulo, shift=UP * 0.15), run_time=0.7)
        self.play(FadeIn(indice, shift=UP * 0.2), run_time=0.9)
        self.wait(1.2)
        self.play(FadeOut(VGroup(titulo, subtitulo, indice)), run_time=0.6)

    # ------------------------------------------------------------------
    # 2. El problema: insertar en un arreglo grande exige mover todo
    #    ~2.0 s (pregunta, sin narración específica)
    #    + 5.0 s → frase 2 (~5.6 s) "Imagina un arreglo con cien mil..."
    #    + 7.0 s → frase 3 (~7.6 s) "...cada elemento debe desplazarse..."
    # ------------------------------------------------------------------
    def _mostrar_problema_arreglo(self):
        pregunta = Text("¿Por qué necesitamos listas enlazadas?", font_size=38)
        self.play(Write(pregunta), run_time=1.0)
        self.wait(0.6)
        self.play(FadeOut(pregunta), run_time=0.4)

        etiqueta_arreglo = Text(
            "Un arreglo con 100 000 elementos guardados uno junto a otro",
            font_size=26,
        ).to_edge(UP, buff=1.1)

        arreglo = self._crear_celdas(("10", "20", "30", "⋯", "99998", "99999"), ancho=1.05)
        arreglo.next_to(etiqueta_arreglo, DOWN, buff=0.7)

        self.play(Write(etiqueta_arreglo), run_time=0.9)
        self.play(FadeIn(arreglo, shift=UP * 0.2, lag_ratio=0.08), run_time=1.3)
        self.wait(1.3)

        instruccion = Text("Queremos insertar un nuevo dato al inicio", font_size=27)
        instruccion.next_to(arreglo, DOWN, buff=0.7)
        self.play(Write(instruccion), run_time=0.9)

        nuevo = self._crear_celdas(("5",), ancho=1.05)[0]
        nuevo.set_stroke(GREEN_C, width=3)
        nuevo.move_to(arreglo.get_left() + LEFT * 1.3)
        self.play(FadeIn(nuevo, shift=RIGHT * 0.2), run_time=0.6)
        self.wait(0.5)

        aviso = Text(
            "Cada uno de los 100 000 elementos debe desplazarse una posición",
            font_size=25,
            color=ORANGE,
        )
        aviso.next_to(instruccion, DOWN, buff=0.4)
        self.play(FadeOut(instruccion), Write(aviso), run_time=1.0)
        # Desplazamiento lento y deliberado: es el punto central del problema.
        self.play(
            arreglo.animate.shift(RIGHT * 1.25),
            *[celda.animate.set_stroke(ORANGE, width=3) for celda in arreglo],
            run_time=2.0,
        )
        self.play(nuevo.animate.move_to(arreglo.get_left() + LEFT * 1.25), run_time=0.8)
        self.wait(1.7)

        self.play(
            FadeOut(VGroup(etiqueta_arreglo, arreglo, nuevo, aviso)),
            run_time=1.0,
        )

    # ------------------------------------------------------------------
    # 3. La solución: la lista enlazada solo agrega una referencia
    #    ~2.0 s → frase 4 (~3.6 s) "Ahora veamos la misma operación..."
    #    + 5.0 s → frase 5 (~5.6 s) "...solo guarda una referencia hacia él."
    #    + 6.0 s → frase 6 (~6.4 s) "...simplemente creamos el nodo..."
    # ------------------------------------------------------------------
    def _mostrar_solucion_lista(self):
        etiqueta_lista = Text(
            "La misma idea con una lista enlazada",
            font_size=28,
            color=GREEN_C,
        ).to_edge(UP, buff=1.1)
        self.play(Write(etiqueta_lista), run_time=1.0)
        self.wait(1.0)

        nodos = self._crear_nodos(("10", "20", "30")).scale(0.82)
        nodos.next_to(etiqueta_lista, DOWN, buff=0.75)
        flechas = VGroup(
            Arrow(nodos[0].get_right(), nodos[1].get_left(), buff=0.1, color=COLOR_PUNTERO),
            Arrow(nodos[1].get_right(), nodos[2].get_left(), buff=0.1, color=COLOR_PUNTERO),
        )
        self.play(FadeIn(nodos, lag_ratio=0.12), run_time=1.2)
        self.play(GrowArrow(flechas[0]), GrowArrow(flechas[1]), run_time=1.0)
        self.wait(1.8)

        instruccion = Text("Insertamos el mismo dato al inicio", font_size=27)
        instruccion.next_to(nodos, DOWN, buff=0.75)
        self.play(Write(instruccion), run_time=0.9)

        nuevo_nodo = self._crear_nodos(("5",))[0].scale(0.82)
        nuevo_nodo.next_to(nodos[0], LEFT, buff=1.5)
        self.play(FadeIn(nuevo_nodo, shift=RIGHT * 0.2), run_time=0.8)

        enlace_nuevo = Arrow(
            nuevo_nodo.get_right(), nodos[0].get_left(), buff=0.1, color=GREEN_C, stroke_width=5
        )
        self.play(GrowArrow(enlace_nuevo), run_time=1.0)
        self.wait(1.0)

        aviso = Text(
            "Ningún otro nodo se mueve: solo se crea una referencia",
            font_size=25,
            color=GREEN_C,
        )
        aviso.next_to(instruccion, DOWN, buff=0.4)
        self.play(
            FadeOut(instruccion),
            Write(aviso),
            Indicate(enlace_nuevo, color=GREEN_C),
            run_time=1.3,
        )
        self.wait(1.0)

        self.play(FadeOut(VGroup(etiqueta_lista, aviso)), run_time=0.5)

        todos_los_nodos = VGroup(nuevo_nodo, *nodos)
        todas_las_flechas = VGroup(enlace_nuevo, *flechas)
        return todos_los_nodos, todas_las_flechas

    # ------------------------------------------------------------------
    # 4. Cierre: qué guarda cada nodo
    #    ~4.4 s → frase 7 (~5.6 s) "Así aparecen los nodos..."
    #    + 4.0 s → frase 8 (~4.4 s) "Ahora veamos la estructura..."
    # ------------------------------------------------------------------
    def _cerrar_concepto(self, nodos, flechas):
        explicacion = Text(
            "Cada nodo guarda un dato y una referencia al siguiente",
            font_size=27,
            color=GREEN_C,
        ).to_edge(DOWN)
        self.play(Write(explicacion), run_time=1.4)

        primer_nodo = nodos[0]
        self.play(
            primer_nodo[1].animate.set_color(COLOR_DATO),
            primer_nodo[3].animate.set_color(COLOR_PUNTERO),
            run_time=0.6,
        )
        self.wait(1.9)

        cierre = Text(
            "Ahora veamos la estructura de una lista enlazada, paso a paso.",
            font_size=27,
        )
        cierre.next_to(explicacion, UP, buff=0.3)
        self.play(Write(cierre), run_time=1.2)
        self.wait(1.8)
        self.play(FadeOut(VGroup(nodos, flechas, explicacion, cierre)), run_time=1.0)

    @staticmethod
    def _crear_celdas(valores, ancho=1.35):
        celdas = VGroup()
        for valor in valores:
            caja = RoundedRectangle(width=ancho, height=0.82, corner_radius=0.12, color=COLOR_NODO)
            texto = Text(str(valor), font_size=26, color=COLOR_DATO).move_to(caja)
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
