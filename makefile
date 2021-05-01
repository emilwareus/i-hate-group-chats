test:
	./ci/runTests.sh

test-full:
	pytest
lint: 
	python -m black .
	flake8 ihgc/**/*.py

