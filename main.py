"""
Punto de entrada principal del proyecto ``greedy_search``.

Ejecuta la búsqueda greedy global y local sobre el conjunto de
estaciones de radio predefinido y muestra los resultados gráficamente.
"""

from src.greedy_search import (
    greedy_search_global,
    greedy_search_local,
    stations,
    needed_states,
)
import src.greedy_search.graficas as plot


def main() -> None:
    """Orquesta la ejecución de ambas búsquedas y su visualización.

    #. Llama a :func:`~greedy_search.main.greedy_search_global` para obtener
       la solución óptima voraz.
    #. Representa el resultado con
       :func:`~greedy_search.graficas.plot_greedy_search_global`.
    #. Llama a :func:`~greedy_search.main.greedy_search_local` para obtener
       los mínimos locales de búsquedas aleatorias.
    #. Representa el resultado con
       :func:`~greedy_search.graficas.plot_greedy_search_local`.

    :rtype: None
    """
    # Búsqueda global: solución voraz con información de progreso
    search_result = greedy_search_global(stations.copy(), needed_states)
    plot.plot_greedy_search_global(*search_result)

    # Búsqueda local: análisis de mínimos locales con muestras aleatorias
    num_uncovered_states = greedy_search_local(stations.copy(), needed_states)
    plot.plot_greedy_search_local(num_uncovered_states)


if __name__ == "__main__":
    main()