import pytest
from src.greedy_search.main import find_best_station
from src.greedy_search.main import greedy_search_global


@pytest.mark.find_best_station
def test_find_best_station():
    # Estados ya cubiertos
    covered_states = set(["wa", "id"])

    # Estaciones y estados que cubren
    stations = {
        "kone": set(["wa", "id", "mt"]),
        "ktwo": set(["or", "nv", "ca"]),
        "kthree": set(["nv", "ut"]),
    }

    best_station, best_gradient = find_best_station(stations, covered_states)

    assert best_station == "ktwo"  # ktwo cubre 3 nuevos estados
    assert best_gradient == 3  # Gradiente esperado es 3


@pytest.mark.find_best_station
def test_find_best_stations():
    """
    En este caso, tanto "kone" como "ktwo" cubren 3 nuevos estados cada una.
    """
    covered_states = set()

    # Estaciones y estados que cubren
    stations = {
        "kone": set(["wa", "id", "mt"]),
        "ktwo": set(["or", "nv", "ca"]),
        "kthree": set(["nv", "ut"]),
    }

    best_station, best_gradient = find_best_station(stations, covered_states)

    assert best_station in {"kone", "ktwo"}
    assert best_gradient == 3  # Gradiente esperado es 3


@pytest.mark.greedy_search_global
def test_greedy_search_global():
    # Estados necesarios
    needed_states = set(["id", "nv", "ut", "mt", "wa", "or", "ca", "az"])

    # Estaciones y estados que cubren
    stations = {
        "kone": set(["id", "nv", "ut"]),
        "ktwo": set(["wa", "id", "mt"]),
        "kthree": set(["or", "nv", "ca"]),
        "kfour": set(["nv", "ut"]),
        "kfive": set(["ca", "az"]),
    }

    stations_needed, num_states_covered, gradients, covered_states = (
        greedy_search_global(stations, needed_states)
    )

    # Se cubren todos los estados necesarios
    assert covered_states == needed_states

    # Todas las estaciones son necesarias menos kfour
    assert set(stations_needed) == {"kone", "ktwo", "kthree", "kfive"}

    # Número de estados cubiertos
    assert num_states_covered[-1] == len(needed_states)

    # Verificar que los gradientes sean consistentes
    assert all(gradient > 0 for gradient in gradients)

    assert gradients == sorted(gradients, reverse=True)
