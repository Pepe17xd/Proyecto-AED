"""Alias compatible para el componente de nodo visual."""

from componentes.nodo_visual import NodoVisual


class NodoLista(NodoVisual):
    """Nombre anterior de :class:`NodoVisual`, conservado por compatibilidad."""

    def __init__(self, valor: object, **kwargs):
        super().__init__(valor, **kwargs)
        self.valor = valor
        self.celda_referencia = self.celda_puntero
