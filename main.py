from src.greedy_search import (
    greedy_search_global,
    greedy_search_local,
    stations,
    needed_states,
)
import src.greedy_search.graficas as plot


def main():
    search_state = greedy_search_global(stations.copy(), needed_states)
    plot.plot_greedy_search_global(*search_state)

    num_uncovered_states = greedy_search_local(stations.copy(), needed_states)
    plot.plot_greedy_search_local(num_uncovered_states)


if __name__ == "__main__":
    main()
