.PHONY: install test lint format

install:
	python -m pip install -U pip
	python -m pip install -e .[dev]

test:
	pytest -q

lint:
	ruff check .

format:
	ruff format .
