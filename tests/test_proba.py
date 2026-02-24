"""
Tests del módulo :mod:`greedy_search.main`.

Verifica el comportamiento de :func:`find_best_station` y
:func:`greedy_search_global` ante distintos escenarios.
"""

import pytest
from src.greedy_search.main import find_best_station, greedy_search_global


# ---------------------------------------------------------------------------
# Tests de find_best_station
# ---------------------------------------------------------------------------


@pytest.mark.find_best_station
def test_find_best_station_con_estados_cubiertos() -> None:
    """Selecciona la estación con mayor gradiente cuando hay estados ya cubiertos.

    Con ``wa`` e ``id`` ya cubiertos, ``ktwo`` (que cubre ``or``, ``nv`` y
    ``ca``) aporta 3 estados nuevos frente a los 1 de ``kone`` y los 2 de
    ``kthree``, por lo que debe ser la ganadora.
    """
    covered_states = {"wa", "id"}
    stations = {
        "kone":   {"wa", "id", "mt"},
        "ktwo":   {"or", "nv", "ca"},
        "kthree": {"nv", "ut"},
    }

    best_station, best_gradient = find_best_station(stations, covered_states)

    assert best_station == "ktwo"
    assert best_gradient == 3


@pytest.mark.find_best_station
def test_find_best_station_sin_estados_cubiertos() -> None:
    """Acepta cualquier estación con gradiente máximo cuando no hay cobertura previa.

    Tanto ``kone`` como ``ktwo`` aportan 3 estados nuevos; el resultado
    puede ser cualquiera de las dos.
    """
    covered_states: set[str] = set()
    stations = {
        "kone":   {"wa", "id", "mt"},
        "ktwo":   {"or", "nv", "ca"},
        "kthree": {"nv", "ut"},
    }

    best_station, best_gradient = find_best_station(stations, covered_states)

    assert best_station in {"kone", "ktwo"}
    assert best_gradient == 3


# ---------------------------------------------------------------------------
# Tests de greedy_search_global
# ---------------------------------------------------------------------------


@pytest.mark.greedy_search_global
def test_greedy_search_global() -> None:
    """Verifica que la búsqueda global cubre todos los estados con el mínimo de estaciones.

    Con el conjunto de estaciones de prueba, la solución óptima greedy debe
    seleccionar ``kone``, ``ktwo``, ``kthree`` y ``kfive`` (excluyendo
    ``kfour`` por ser redundante) y cubrir los 8 estados requeridos.
    """
    needed_states = {"id", "nv", "ut", "mt", "wa", "or", "ca", "az"}
    stations = {
        "kone":   {"id", "nv", "ut"},
        "ktwo":   {"wa", "id", "mt"},
        "kthree": {"or", "nv", "ca"},
        "kfour":  {"nv", "ut"},
        "kfive":  {"ca", "az"},
    }

    stations_needed, num_states_covered, gradients, covered_states = greedy_search_global(
        stations, needed_states
    )

    assert covered_states == needed_states
    assert set(stations_needed) == {"kone", "ktwo", "kthree", "kfive"}
    assert num_states_covered[-1] == len(needed_states)
    assert all(g > 0 for g in gradients)
    assert gradients == sorted(gradients, reverse=True)