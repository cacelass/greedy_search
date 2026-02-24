import matplotlib.pyplot as plt


def plot_greedy_search_global(
    stations_needed, num_states_covered, gradients, covered_states
):
    print(f"covered states: {covered_states}")
    print(f"stations needed: {stations_needed}")
    print(f"num states covered: {num_states_covered}")
    print(f"gradients: {gradients}")

    # Crear la visualización
    plt.figure(figsize=(12, 6))

    # Crear el primer eje para las barras
    ax1 = plt.gca()
    ax1.bar(stations_needed, gradients, color="skyblue", label="Nuevos estados")
    ax1.set_ylabel("Nuevos estados cubiertos", color="skyblue")
    ax1.tick_params(axis="y", labelcolor="skyblue")

    # Crear el segundo ej/home/a25alejandrocc/Documentos/MIA/profe/greedy-search/main.pye para la línea
    ax2 = ax1.twinx()
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

    # Combinar leyendas de ambos ejes
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

    plt.tight_layout()
    plt.show()


def plot_greedy_search_local(
    num_uncovered_states,
):
    print(f"num states uncovered: {num_uncovered_states}")

    plt.figure(figsize=(10, 6))
    plt.bar(range(len(num_uncovered_states)), num_uncovered_states)
    plt.title("Mínimos locales en la búsqueda local")
    plt.xlabel("Iteracion")
    plt.ylabel("Número de estados sin cubrir")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()
