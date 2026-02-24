.PHONY: setup test docs lint clean

setup:
	uv sync --extra dev --extra ml 

test:
	uv run pytest

lint:
	uv run ruff check src tests

docs:
	sphinx-apidoc -o docs/source/ src
	make html -C docs

clean:
	rm -rf .venv .pytest_cache docs/build .venv
