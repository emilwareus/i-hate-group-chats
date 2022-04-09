#!/bin/sh

set -e

poetry install

# Lint
flake8 ihgc/**/*.py

# Unit tests
pytest -m "not integtest" 