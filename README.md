# greedy_search

**Autor:** Alejandro Cancelas Chapela

Implementación del algoritmo de búsqueda voraz (*greedy search*) aplicado al
**Set Covering Problem**: dado un conjunto de estados de EE.UU. que se quieren
cubrir y un catálogo de estaciones de radio con su área de cobertura, se
selecciona el subconjunto mínimo de estaciones que cubra todos los estados
objetivo.

El proyecto incluye dos variantes del algoritmo, visualización de resultados
con Matplotlib y una suite de tests con Pytest.

---

## Tabla de contenidos

- [Descripción del problema](#descripción-del-problema)
- [Algoritmos implementados](#algoritmos-implementados)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Tests](#tests)
- [Documentación](#documentación)

---

## Descripción del problema

Se tienen 22 estados de EE.UU. (oeste, centro y sur) que deben quedar cubiertos
por al menos una estación de radio. Cada estación cubre un subconjunto de
estados. El objetivo es encontrar el conjunto más pequeño de estaciones que
garantice cobertura total.

Este es un problema NP-completo en su forma exacta; el algoritmo greedy
ofrece una solución aproximada eficiente con garantía de
`(1 - 1/e) ≈ 63 %` del óptimo.

---

## Algoritmos implementados

### Búsqueda greedy global (`greedy_search_global`)

En cada iteración elige la estación que cubre el mayor número de estados
**aún sin cubrir** (máximo gradiente local). Se repite hasta cubrir todos
los estados objetivo.

- **Ventaja:** solución determinista y de calidad garantizada.
- **Complejidad:** `O(n · m)` donde `n` = estaciones y `m` = estados.

### Búsqueda greedy local (`greedy_search_local`)

Ejecuta `N` iteraciones aleatorias seleccionando cada vez un subconjunto
de estaciones al azar y registrando cuántos estados quedan sin cubrir.
Permite visualizar la distribución de mínimos locales.

- **Ventaja:** ilustra el problema de los mínimos locales en búsquedas
  no dirigidas.
- Parámetros configurables: número de iteraciones (`num_searches`) y
  tamaño del subconjunto (`max_stations`).

---

## Estructura del proyecto

```
greedy_search/
├── main.py                  # Punto de entrada
├── pyproject.toml
├── README.md
├── docs/
│   └── source/
│       ├── conf.py
│       └── index.rst
├── src/
│   └── greedy_search/
│       ├── __init__.py      # API pública del paquete
│       ├── __main__.py
│       ├── main.py          # Lógica del algoritmo
│       └── graficas.py      # Visualización con Matplotlib
└── tests/
    └── test_proba.py        # Tests con Pytest
```

---

## Requisitos

- Python `>= 3.10`
- Las dependencias se gestionan con [Hatch](https://hatch.pypa.io/)

**Dependencias de desarrollo** (`dev`):
`ruff`, `pytest`, `pytest-cov`, `pytest-sugar`, `sphinx`, `sphinx-rtd-theme`, `ty`

**Dependencias de visualización** (`ml`):
`matplotlib`

---

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/cacelass/greedy_search
cd greedy_search

# Instalar con todas las dependencias
make setup
```

---

## Uso

### Ejecutar el programa principal

```bash
uv run python3 main.py
```

Esto ejecutará la búsqueda greedy global y la local, mostrando un gráfico
para cada una.

### Usar el paquete como módulo

```python
from greedy_search import greedy_search_global, greedy_search_local, stations, needed_states

# Búsqueda global
stations_needed, num_covered, gradients, covered = greedy_search_global(
    stations.copy(), needed_states
)
print(f"Estaciones seleccionadas: {stations_needed}")
print(f"Estados cubiertos: {len(covered)}/{len(needed_states)}")

# Búsqueda local (40 iteraciones, 10 estaciones aleatorias cada una)
uncovered_per_iteration = greedy_search_local(
    stations.copy(), needed_states, num_searches=40, max_stations=10
)
```

### Usar con datos propios

```python
from greedy_search import greedy_search_global

mis_estaciones = {
    "radio_a": {"madrid", "toledo"},
    "radio_b": {"barcelona", "tarragona"},
    "radio_c": {"madrid", "barcelona", "valencia"},
}
estados_objetivo = {"madrid", "barcelona", "valencia", "toledo", "tarragona"}

resultado = greedy_search_global(mis_estaciones, estados_objetivo)
print(resultado[0])  # estaciones seleccionadas
```

---

## Tests

```bash
# Ejecutar todos los tests
pytest

# Con cobertura
pytest --cov=src/greedy_search

# Filtrar por marca
pytest -m find_best_station
pytest -m greedy_search_global
```

Los tests cubren:
- Selección de la mejor estación con y sin estados ya cubiertos.
- Corrección de la solución global (cobertura total, no redundancia, gradientes decrecientes).

---

## Documentación

La documentación se genera con [Sphinx](https://www.sphinx-doc.org/) en formato
HTML a partir de los docstrings del código.

```bash
cd docs
make html
```

La documentación generada estará disponible en `docs/build/html/index.html`.

Todos los módulos, funciones y datos públicos están documentados siguiendo el
estilo reStructuredText compatible con Sphinx, incluyendo tipos (`:type:`),
parámetros (`:param:`), valores de retorno (`:return:`) y ejemplos de uso.