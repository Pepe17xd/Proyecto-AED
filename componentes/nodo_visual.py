"""Nodo visual autocontenido para animaciones de estructuras enlazadas."""

from manim import AnimationGroup, Arrow, Create, FadeOut, RIGHT, Rectangle, Text, VGroup

from config.estilo import ALTO_NODO, ANCHO_NODO, COLOR_DATO, COLOR_NODO, COLOR_PUNTERO


class NodoVisual(VGroup):
    """Representa un nodo con dato y puntero `next`.

    La clase no necesita conocer la lista completa. Una escena puede crear
        nodos, posicionarlos y pedirle al nodo que se conecte a otro::

        self.play(origen.animar_conexion(destino))

    Los enlaces se actualizan si el nodo origen o destino cambia de posición.
    """

    def __init__(self, dato: object, **kwargs):
        super().__init__(**kwargs)
        self.dato = dato
        self.conexiones_salientes = VGroup()

        self.celda_dato = Rectangle(
            width=ANCHO_NODO, height=ALTO_NODO, color=COLOR_NODO
        )
        self.celda_puntero = Rectangle(
            width=ANCHO_NODO * 0.42, height=ALTO_NODO, color=COLOR_NODO
        ).next_to(self.celda_dato, RIGHT, buff=0)
        self.etiqueta = Text(str(dato), font_size=30, color=COLOR_DATO).move_to(self.celda_dato)
        self.add(self.celda_dato, self.celda_puntero, self.etiqueta)

    @property
    def puerto_salida(self):
        """Anclaje para flechas que parten de la referencia del nodo."""
        return self.celda_puntero.get_right()

    def animar_creacion(self, **kwargs):
        """Devuelve la animación de aparición del nodo.

        Se usa como ``self.play(nodo.animar_creacion())``.
        """
        return Create(self, **kwargs)

    def conectar_a(self, destino: "NodoVisual", **kwargs):
        """Crea y registra la flecha dirigida hacia ``destino``.

        La flecha no se añade automáticamente a la escena: use la animación
        devuelta por ``animar_conexion`` o añádala manualmente con ``self.add``.
        """
        flecha = Arrow(
            self.puerto_salida,
            destino.get_left(),
            buff=0.08,
            color=COLOR_PUNTERO,
            stroke_width=4,
            **kwargs,
        )
        flecha.add_updater(
            lambda mob: mob.put_start_and_end_on(self.puerto_salida, destino.get_left())
        )
        self.conexiones_salientes.add(flecha)
        return flecha

    def animar_conexion(self, destino: "NodoVisual", **kwargs):
        """Crea la conexión y devuelve su animación de dibujo.

        La flecha queda disponible en ``conexiones_salientes`` para resaltarla,
        reemplazarla o eliminarla más adelante.
        """
        return Create(self.conectar_a(destino, **kwargs))

    def animar_eliminacion(self, eliminar_conexiones=True, **kwargs):
        """Devuelve una animación para retirar el nodo y sus enlaces salientes."""
        animaciones = [FadeOut(self, **kwargs)]
        if eliminar_conexiones:
            for conexion in self.conexiones_salientes:
                conexion.clear_updaters()
                animaciones.append(FadeOut(conexion, **kwargs))
        return AnimationGroup(*animaciones)
