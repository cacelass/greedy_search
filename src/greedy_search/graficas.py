"""
Módulo de visualización para los resultados de la búsqueda greedy.

Proporciona funciones para representar gráficamente tanto la búsqueda
global (progreso acumulado de cobertura) como la local (distribución
de mínimos locales entre iteraciones aleatorias).
"""

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from .main import StationName, StateName


def plot_greedy_search_global(
    stations_needed: list[StationName],
    num_states_covered: list[int],
    gradients: list[int],
    covered_states: set[StateName],
) -> None:
    """Representa gráficamente el progreso de la búsqueda greedy global.

    Genera un gráfico con dos ejes Y compartiendo el eje X:

    * **Barras (azul)** Nuevos estados aportados por cada estación
      seleccionada (*gradiente*).
    * **Línea (rojo)** Total acumulado de estados cubiertos tras cada
      selección.

    Adicionalmente imprime por consola un resumen de los resultados.

    :param stations_needed: Lista de estaciones seleccionadas en orden de
        elección.
    :type stations_needed: list[StationName]
    :param num_states_covered: Número acumulado de estados cubiertos tras
        cada selección.
    :type num_states_covered: list[int]
    :param gradients: Número de estados nuevos aportados por cada estación.
    :type gradients: list[int]
    :param covered_states: Conjunto final de todos los estados cubiertos.
    :type covered_states: set[StateName]
    :rtype: None
    """
    print(f"covered states:     {covered_states}")
    print(f"stations needed:    {stations_needed}")
    print(f"num states covered: {num_states_covered}")
    print(f"gradients:          {gradients}")

    fig: Figure
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Eje izquierdo: gradientes (barras)
    ax1.bar(stations_needed, gradients, color="skyblue", label="Nuevos estados")
    ax1.set_ylabel("Nuevos estados cubiertos", color="skyblue")
    ax1.tick_params(axis="y", labelcolor="skyblue")

    # Eje derecho: total acumulado (línea)
    ax2: Axes = ax1.twinx()
    ax2.plot(
        stations_needed,
        num_states_covered,
        color="red",
        marker="o",
        label="Total estados",
    )
    ax2.set_ylabel("Total estados cubiertos", color="red")
    ax2.tick_params(axis="y", labelcolor="red")

    plt.title("Progreso de la cobertura por estación")
    plt.xticks(rotation=45)

    # Combinar leyendas de ambos ejes en una sola
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

    plt.tight_layout()
    plt.show()


def plot_greedy_search_local(num_uncovered_states: list[int]) -> None:
    """Representa gráficamente los resultados de la búsqueda greedy local.

    Muestra un gráfico de barras donde cada barra corresponde a una
    iteración aleatoria e indica cuántos estados quedaron sin cubrir,
    permitiendo visualizar la distribución de mínimos locales.

    :param num_uncovered_states: Lista con el número de estados sin cubrir
        en cada iteración.
    :type num_uncovered_states: list[int]
    :rtype: None
    """
    print(f"num states uncovered: {num_uncovered_states}")

    plt.figure(figsize=(10, 6))
    plt.bar(range(len(num_uncovered_states)), num_uncovered_states)
    plt.title("Mínimos locales en la búsqueda local")
    plt.xlabel("Iteración")
    plt.ylabel("Número de estados sin cubrir")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()