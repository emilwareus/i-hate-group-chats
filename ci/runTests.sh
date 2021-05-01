#!/bin/sh

set -e

pip install -r requirements.txt
pip install -r requirements-test.txt

# Lint
flake8 ihgc/**/*.py

# Unit tests
pytest -m "not integtest" 