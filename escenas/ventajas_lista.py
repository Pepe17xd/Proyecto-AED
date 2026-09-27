"""Ventajas visuales de una lista enlazada simple."""

from manim import Create, DOWN, FadeOut, GREEN, Indicate, Rectangle, RIGHT, Text, UP, VGroup, Write

from config.estilo import COLOR_DATO, COLOR_NODO
from escenas.base import EscenaListaEnlazada
from estructuras.lista_enlazada_visual import ListaEnlazadaVisual


class VentajasLista(EscenaListaEnlazada):
    def construct(self):
        self.mostrar_titulo("Ventajas de las listas enlazadas")

        encabezado = Text("1. Tamaño dinámico", font_size=30).to_edge(UP).shift(DOWN * 1.0)
        lista = self._lista((10, 20, 30))
        self.play(Write(encabezado), lista.animar_creacion_lista())
        nuevo = lista.agregar(40)
        self.play(nuevo.animar_creacion(), Create(lista.enlaces[-1]))
        mensaje = Text("La lista puede crecer dinámicamente.", font_size=26, color=GREEN).to_edge(DOWN)
        self.play(Write(mensaje), Indicate(nuevo, color=GREEN))
        self.play(FadeOut(encabezado), FadeOut(mensaje), FadeOut(lista))

        encabezado = Text("2. Inserción y eliminación eficiente", font_size=30).to_edge(UP).shift(DOWN * 1.0)
        lista = self._lista((10, 20, 30))
        self.play(Write(encabezado), lista.animar_creacion_lista())
        self.play(lista.insertar(15, 2))
        mensaje = Text("Solo cambian referencias.", font_size=27, color=GREEN).to_edge(DOWN)
        self.play(Write(mensaje), Indicate(lista.enlaces[0], color=GREEN))
        self.play(FadeOut(encabezado), FadeOut(mensaje), FadeOut(lista))

        encabezado = Text("3. No necesita memoria contigua", font_size=30).to_edge(UP).shift(DOWN * 1.0)
        arreglo = self._arreglo((10, 20, 30)).shift(UP * 1.0)
        lista = self._lista((10, 20, 30)).shift(DOWN * 1.0)
        self.play(Write(encabezado), Create(arreglo))
        self.play(lista.animar_creacion_lista())
        self.play(Write(Text("Arreglo", font_size=23).next_to(arreglo, UP)), Write(Text("Lista: conexiones mediante referencias", font_size=23).next_to(lista, DOWN)))
        self.wait(1)

    @staticmethod
    def _lista(valores):
        lista = ListaEnlazadaVisual()
        for valor in valores:
            lista.agregar(valor)
        return lista

    @staticmethod
    def _arreglo(valores):
        celdas = VGroup()
        for valor in valores:
            celda = Rectangle(width=1.1, height=0.7, color=COLOR_NODO)
            celdas.add(VGroup(celda, Text(str(valor), font_size=27, color=COLOR_DATO).move_to(celda)))
        return celdas.arrange(RIGHT, buff=0)
