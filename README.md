# Adaptive Multimodal AI Serving Platform

This project provides a production-oriented platform for adaptive multimodal AI serving with scheduling, dispatch, worker lifecycle management, telemetry, and benchmark/research workflow separation.

## Structure

- `src/adaptive_serving` contains core service logic and domain abstractions.
- `services` contains independently deployable service entrypoints.
- `research` contains offline experiments and analysis artifacts.
- `benchmarks`, `configs`, `tests`, and `docs` support benchmarking, configuration, validation, and documentation.

## Getting started

1. Create a virtual environment.
2. Install dependencies with `pip install -e .` or `uv sync`.
3. Review the configuration files under `configs/`.
4. Run the gateway service with `python services/gateway/main.py`.
