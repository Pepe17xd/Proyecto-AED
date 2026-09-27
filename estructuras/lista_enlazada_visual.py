"""Gestión visual y animable de una lista simplemente enlazada."""

from __future__ import annotations

from manim import (
    AnimationGroup,
    Create,
    FadeOut,
    ORIGIN,
    RIGHT,
    UP,
    Succession,
    VGroup,
)

from componentes.nodo_visual import NodoVisual
from config.estilo import ESPACIO_NODOS


class ListaEnlazadaVisual(VGroup):
    """Lista simplemente enlazada compuesta por :class:`NodoVisual`.

    Las posiciones públicas son **1-indexadas**: ``insertar(15, 2)`` añade el
    valor 15 como segundo nodo y ``eliminar(2)`` retira el segundo nodo.
    Los métodos que modifican la estructura devuelven una animación para usar
    directamente con ``Scene.play``.
    """

    def __init__(self, espaciado: float = ESPACIO_NODOS, **kwargs):
        super().__init__(**kwargs)
        self.espaciado = espaciado
        self.nodos: list[NodoVisual] = []
        self.enlaces = VGroup()
        self._enlace_por_origen: dict[NodoVisual, object] = {}
        self.add(self.enlaces)

    def agregar(self, valor: object) -> NodoVisual:
        """Añade ``valor`` al final y crea su enlace desde el antiguo último."""
        centro = self._centro_actual()
        nuevo = NodoVisual(valor)
        anterior = self.nodos[-1] if self.nodos else None

        self.nodos.append(nuevo)
        self.add(nuevo)
        if anterior is not None:
            self._crear_enlace(anterior, nuevo)
        self.posicionar_nodos(centro=centro)
        return nuevo

    def posicionar_nodos(self, centro=None) -> None:
        """Distribuye los nodos horizontalmente alrededor de ``centro``.

        Si no se indica centro, se conserva el centro visual de los nodos ya
        presentes. Esto permite mover la lista en una escena y después añadir,
        insertar o eliminar sin que vuelva al origen.
        """
        centro = self._centro_actual() if centro is None else centro
        for nodo, posicion in zip(self.nodos, self._posiciones_objetivo(centro)):
            nodo.move_to(posicion)

    def animar_creacion_lista(self):
        """Devuelve nodos y enlaces en el orden pedagógico de aparición."""
        pasos = []
        for indice, nodo in enumerate(self.nodos):
            pasos.append(nodo.animar_creacion())
            if indice:
                enlace = self._enlace_por_origen[self.nodos[indice - 1]]
                pasos.append(Create(enlace))
        return Succession(*pasos) if pasos else AnimationGroup()

    def insertar(self, valor: object, posicion: int):
        """Inserta un nodo y devuelve la animación de actualización visual."""
        self._validar_posicion_insercion(posicion)
        indice = posicion - 1
        centro = self._centro_actual()
        anterior = self.nodos[indice - 1] if indice else None
        siguiente = self.nodos[indice] if indice < len(self.nodos) else None

        nuevo = NodoVisual(valor)
        self.nodos.insert(indice, nuevo)
        self.add(nuevo)
        destinos = self._posiciones_objetivo(centro)
        nuevo.move_to(destinos[indice] + UP * 1.4)

        enlace_antiguo = self._quitar_enlace(anterior) if anterior and siguiente else None
        enlaces_nuevos = []
        if anterior:
            enlaces_nuevos.append(self._crear_enlace(anterior, nuevo))
        if siguiente:
            enlaces_nuevos.append(self._crear_enlace(nuevo, siguiente))

        cambios_enlaces = [FadeOut(enlace_antiguo)] if enlace_antiguo else []
        cambios_enlaces.extend(Create(enlace) for enlace in enlaces_nuevos)
        reposicionamiento = self._animar_reposicionamiento(destinos)

        pasos = [nuevo.animar_creacion()]
        if cambios_enlaces:
            pasos.append(AnimationGroup(*cambios_enlaces))
        if reposicionamiento:
            pasos.append(AnimationGroup(*reposicionamiento))
        return Succession(*pasos)

    def eliminar(self, posicion: int):
        """Elimina el nodo indicado y devuelve la animación de reconexión."""
        self._validar_posicion_existente(posicion)
        indice = posicion - 1
        centro = self._centro_actual()
        eliminado = self.nodos[indice]
        anterior = self.nodos[indice - 1] if indice else None
        siguiente = self.nodos[indice + 1] if indice + 1 < len(self.nodos) else None

        enlace_entrante = self._quitar_enlace(anterior) if anterior else None
        # El enlace saliente pertenece al nodo eliminado. Se retira de la
        # estructura lógica, pero se conserva en el nodo para que su propia
        # animación lo desvanezca junto con el nodo.
        enlace_saliente = self._enlace_por_origen.pop(eliminado, None)
        if enlace_saliente:
            self.enlaces.remove(enlace_saliente)
        self.nodos.pop(indice)
        self.remove(eliminado)
        destinos = self._posiciones_objetivo(centro)

        enlace_nuevo = self._crear_enlace(anterior, siguiente) if anterior and siguiente else None
        desapariciones = [eliminado.animar_eliminacion()]
        if enlace_entrante:
            desapariciones.append(FadeOut(enlace_entrante))
        reposicionamiento = self._animar_reposicionamiento(destinos)

        pasos = [AnimationGroup(*desapariciones)]
        if enlace_nuevo:
            pasos.append(Create(enlace_nuevo))
        if reposicionamiento:
            pasos.append(AnimationGroup(*reposicionamiento))
        return Succession(*pasos)

    def _crear_enlace(self, origen: NodoVisual, destino: NodoVisual):
        """Crea y registra una única flecha saliente para ``origen``."""
        enlace = origen.conectar_a(destino)
        self.enlaces.add(enlace)
        self._enlace_por_origen[origen] = enlace
        return enlace

    def _quitar_enlace(self, origen: NodoVisual | None):
        """Desregistra el enlace saliente de ``origen`` sin eliminarlo aún."""
        if origen is None:
            return None
        enlace = self._enlace_por_origen.pop(origen, None)
        if enlace is None:
            return None
        enlace.clear_updaters()
        self.enlaces.remove(enlace)
        origen.conexiones_salientes.remove(enlace)
        return enlace

    def _centro_actual(self):
        if not self.nodos:
            return ORIGIN.copy()
        return (self.nodos[0].get_center() + self.nodos[-1].get_center()) / 2

    def _posiciones_objetivo(self, centro):
        if not self.nodos:
            return []
        paso = self.nodos[0].width + self.espaciado
        desplazamiento_inicial = -paso * (len(self.nodos) - 1) / 2
        return [centro + RIGHT * (desplazamiento_inicial + paso * i) for i in range(len(self.nodos))]

    def _animar_reposicionamiento(self, destinos):
        return [
            nodo.animate.move_to(destino)
            for nodo, destino in zip(self.nodos, destinos)
            if not nodo.get_center().round(6).tolist() == destino.round(6).tolist()
        ]

    def _validar_posicion_insercion(self, posicion: int) -> None:
        if not isinstance(posicion, int) or not 1 <= posicion <= len(self.nodos) + 1:
            raise IndexError(f"La posición de inserción debe estar entre 1 y {len(self.nodos) + 1}.")

    def _validar_posicion_existente(self, posicion: int) -> None:
        if not isinstance(posicion, int) or not 1 <= posicion <= len(self.nodos):
            raise IndexError(f"La posición debe estar entre 1 y {len(self.nodos)}.")
