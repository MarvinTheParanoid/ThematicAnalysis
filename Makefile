VENV = .venv
.DEFAULT_GOAL := help

## Print list of commands and exit
# This command prints all the commands in the Makefile and their descriptions
# which are all the lines in the file that start with a double hash ##
help:
	@awk '/^##.*$$/,/^[~\/\.a-zA-Z_-]+:/' $(MAKEFILE_LIST) | \
	awk '!/^(# )/' | \
	awk '!(NR%2){print $$0p}{p=$$0}' | \
	awk 'BEGIN {FS = ":.*?##"}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' | \
	sort

## Run a jupyter labs server
notebook:
	@uv run --with jupyter jupyter lab

## Run ruff lint
lint:
	@uv run ruff check . --fix

## Run ruff format
fmt:
	@uv run ruff format .

## Run pre-commit checks
check:
	@pre-commit run --all-files
