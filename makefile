test:
	bash ./ci/runTests.sh

lint: 
	python -m black .
	flake8 ihgc/**/*.py

