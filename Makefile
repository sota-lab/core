.PHONY : install
install:
	poetry install

.PHONY : format
format :
	isort .
	black .

.PHONY : lint
lint:
	flake8 .
	mypy .
