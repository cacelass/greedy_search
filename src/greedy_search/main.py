"""
Módulo principal del algoritmo de búsqueda greedy.

Implementa la búsqueda greedy global y local para seleccionar
el conjunto mínimo de estaciones de radio que cubran todos los
estados objetivo de EE.UU.
"""

import random
from typing import TypeAlias

# ---------------------------------------------------------------------------
# Tipos personalizados
# ---------------------------------------------------------------------------

StationName: TypeAlias = str
StateName: TypeAlias = str
StationsMap: TypeAlias = dict[StationName, set[StateName]]
SearchResult: TypeAlias = tuple[list[StationName], list[int], list[int], set[StateName]]

# ---------------------------------------------------------------------------
# Datos: estados y estaciones
# ---------------------------------------------------------------------------

#: Estados del oeste de EE.UU. que se deben cubrir inicialmente.
WESTERN_STATES: set[StateName] = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

#: Estados del centro y sur que se añaden al objetivo.
CENTRAL_STATES: set[StateName] = {
    "nm", "tx", "ok", "ks", "co", "ne", "sd", "wy",
    "nd", "ia", "mn", "mo", "ar", "la",
}

#: Conjunto total de estados que deben quedar cubiertos al final.
needed_states: set[StateName] = WESTERN_STATES | CENTRAL_STATES

#: Mapa de estaciones de radio y los estados que cada una cubre.
stations: StationsMap = {
    "kone":      {"id", "nv", "ut"},
    "ktwo":      {"wa", "id", "mt"},
    "kthree":    {"or", "nv", "ca"},
    "kfour":     {"nv", "ut"},
    "kfive":     {"ca", "az"},
    "ksix":      {"nm", "tx", "ok"},
    "kseven":    {"ok", "ks", "co"},
    "keight":    {"ks", "co", "ne"},
    "knine":     {"ne", "sd", "wy"},
    "kten":      {"nd", "ia"},
    "keleven":   {"mn", "mo", "ar"},
    "ktwelve":   {"la"},
    "kthirteen": {"mo", "ar"},
}

# ---------------------------------------------------------------------------
# Funciones
# ---------------------------------------------------------------------------


def find_best_station(
    stations: StationsMap,
    covered_states: set[StateName],
) -> tuple[StationName, int]:
    """Encuentra la estación que cubre la mayor cantidad de estados aún sin cubrir.

    Calcula el *gradiente* de cada estación (número de estados nuevos que
    aportaría) y devuelve la que maximiza dicho valor.

    :param stations: Mapa de estaciones disponibles y sus estados cubiertos.
    :type stations: StationsMap
    :param covered_states: Conjunto de estados ya cubiertos.
    :type covered_states: set[StateName]
    :return: Tupla ``(nombre_estación, gradiente_máximo)``.
    :rtype: tuple[StationName, int]

    Ejemplo::

        >>> find_best_station({"k1": {"a", "b"}, "k2": {"b", "c"}}, {"b"})
        ('k2', 1)
    """
    gradients: dict[StationName, int] = {
        station: len(states - covered_states)
        for station, states in stations.items()
    }
    best_station: StationName = max(gradients, key=gradients.get, default="")
    return best_station, gradients[best_station]


def greedy_search_global(
    stations: StationsMap,
    needed_states: set[StateName],
) -> SearchResult:
    """Ejecuta la búsqueda greedy global para cubrir todos los estados requeridos.

    En cada iteración selecciona la estación que cubre la mayor cantidad de
    estados nuevos (estrategia voraz global) hasta que todos los estados
    objetivo estén cubiertos.

    :param stations: Mapa completo de estaciones y sus estados.
    :type stations: StationsMap
    :param needed_states: Conjunto de estados que deben quedar cubiertos.
    :type needed_states: set[StateName]
    :return: Tupla con:

        - **stations_needed** – Lista ordenada de estaciones seleccionadas.
        - **num_states_covered** – Número acumulado de estados cubiertos tras
          cada selección.
        - **gradients** – Gradiente (estados nuevos) aportado por cada estación
          seleccionada.
        - **covered_states** – Conjunto final de estados cubiertos.

    :rtype: SearchResult
    """
    remaining: StationsMap = stations.copy()
    covered_states: set[StateName] = set()
    stations_needed: list[StationName] = []
    gradients: list[int] = []
    num_states_covered: list[int] = []

    while covered_states < needed_states:
        best_station, best_gradient = find_best_station(remaining, covered_states)

        if not best_station:
            break

        covered_states |= remaining.pop(best_station)
        stations_needed.append(best_station)
        gradients.append(best_gradient)
        num_states_covered.append(len(covered_states))

    return stations_needed, num_states_covered, gradients, covered_states


def greedy_search_local(
    stations: StationsMap,
    needed_states: set[StateName],
    num_searches: int = 40,
    max_stations: int = 10,
) -> list[int]:
    """Ejecuta múltiples búsquedas greedy locales con selección aleatoria.

    En cada iteración se elige un subconjunto aleatorio de estaciones y se
    registra cuántos estados quedan sin cubrir, permitiendo analizar la
    distribución de mínimos locales.

    :param stations: Mapa completo de estaciones y sus estados.
    :type stations: StationsMap
    :param needed_states: Conjunto de estados que deben quedar cubiertos.
    :type needed_states: set[StateName]
    :param num_searches: Número de iteraciones aleatorias. Por defecto ``40``.
    :type num_searches: int
    :param max_stations: Tamaño del subconjunto aleatorio por iteración.
        Por defecto ``10``.
    :type max_stations: int
    :return: Lista con el número de estados sin cubrir en cada iteración.
    :rtype: list[int]
    """
    station_names: list[StationName] = list(stations.keys())
    num_uncovered: list[int] = []

    for _ in range(num_searches):
        covered: set[StateName] = set()
        for station in random.sample(station_names, k=max_stations):
            covered |= stations[station]
        num_uncovered.append(len(needed_states - covered))

    return num_uncovered