"""Desventajas visuales de una lista enlazada simple."""

from manim import Create, DOWN, FadeOut, GREEN, Indicate, Rectangle, RIGHT, Text, Transform, UP, VGroup, Write

from componentes.nodo_visual import NodoVisual
from config.estilo import COLOR_DATO, COLOR_NODO
from escenas.base import EscenaListaEnlazada
from estructuras.lista_enlazada_visual import ListaEnlazadaVisual


class DesventajasLista(EscenaListaEnlazada):
    def construct(self):
        self.mostrar_titulo("Desventajas de las listas enlazadas")

        encabezado = Text("1. Acceso secuencial", font_size=30).to_edge(UP).shift(DOWN * 1.0)
        arreglo = self._arreglo().shift(UP * 1.0)
        lista = self._lista().shift(DOWN * 1.0)
        self.play(Write(encabezado), Create(arreglo), lista.animar_creacion_lista())
        directo = Text("Posición 3: acceso directo", font_size=24, color=GREEN).next_to(arreglo, UP)
        self.play(Write(directo), Indicate(arreglo[2], color=GREEN))
        self.play(Indicate(lista.nodos[0]), Indicate(lista.nodos[1]), Indicate(lista.nodos[2]))
        secuencial = Text("Para llegar a 30: revisar 10, 20 y 30", font_size=24).next_to(lista, DOWN)
        self.play(Write(secuencial))
        self.play(FadeOut(encabezado), FadeOut(arreglo), FadeOut(lista), FadeOut(directo), FadeOut(secuencial))

        encabezado = Text("2. Mayor uso de memoria", font_size=30).to_edge(UP).shift(DOWN * 1.0)
        dato = VGroup(Rectangle(width=1.4, height=0.85, color=COLOR_NODO), Text("10", font_size=30, color=COLOR_DATO)).move_to(UP * 0.2)
        dato[1].move_to(dato[0])
        nodo = NodoVisual(10).move_to(UP * 0.2)
        self.play(Write(encabezado), Create(dato))
        self.play(Transform(dato, nodo))
        mensaje = Text("Cada nodo almacena información adicional.", font_size=25).to_edge(DOWN)
        self.play(Write(mensaje), Indicate(nodo.celda_puntero, color=GREEN))
        self.play(FadeOut(encabezado), FadeOut(dato), FadeOut(mensaje))

        encabezado = Text("3. Mayor complejidad", font_size=30).to_edge(UP).shift(DOWN * 1.0)
        lista = self._lista()
        self.play(Write(encabezado), lista.animar_creacion_lista())
        self.play(Indicate(lista.enlaces[0], color=GREEN), Indicate(lista.enlaces[1], color=GREEN))
        self.play(Write(Text("Los enlaces deben mantenerse correctamente.", font_size=25).to_edge(DOWN)))
        self.wait(1)

    @staticmethod
    def _lista():
        lista = ListaEnlazadaVisual()
        for valor in (10, 20, 30):
            lista.agregar(valor)
        return lista

    @staticmethod
    def _arreglo():
        celdas = VGroup()
        for valor in (10, 20, 30):
            marco = Rectangle(width=1.1, height=0.7, color=COLOR_NODO)
            celdas.add(VGroup(marco, Text(str(valor), font_size=27, color=COLOR_DATO).move_to(marco)))
        return celdas.arrange(RIGHT, buff=0)
