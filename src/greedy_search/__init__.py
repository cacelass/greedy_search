"""
Paquete ``greedy_search``.

Exporta los símbolos públicos del módulo principal para facilitar
las importaciones desde el paquete raíz.

Símbolos exportados:

- :data:`stations` – Mapa de estaciones y estados cubiertos.
- :data:`needed_states` – Conjunto de estados objetivo.
- :func:`greedy_search_global` – Búsqueda voraz global.
- :func:`greedy_search_local` – Búsqueda voraz local aleatoria.
"""

from .main import stations, needed_states, greedy_search_global, greedy_search_local

__all__ = [
    "stations",
    "needed_states",
    "greedy_search_global",
    "greedy_search_local",
]