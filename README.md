# Thematic Analysis

A simple application demonstrating an approach to extracting themes from text data. This project focuses on analyzing open-text responses to identify recurring themes and patterns. Currently a work in progress and not in a fully working state.

## Setup

### Requirement

- Python>=3.13
- UV (recommended)
- Docker
- GNU Make

### Installing

```shell
git clone <repo>
cd <repo-name>

# Using UV (recommended)
uv sync

# Using pip on Windows
python -m venv .venv
.\.venv\Scripts\activate
pip install -e .[dev]

# Using pip on Linux/OSX
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

### Running

```shell
# With docker
docker compose up --build

# With uv
uv run python src/thematic_analysis/app.py

# Using pip on Windows
.\.venv\Scripts\activate
python -m src.thematic_analysis.app

# Using pip on Linux/OSX
source .venv/bin/activate
python -m src.thematic_analysis.app
```

## Problem

Summarized Problem Statement:

You are given a dataset (walmart.csv) containing three columns of open-text responses. The task is to perform thematic analysis (also known as "theme counting") by identifying recurring themes within one or all of these columns.

For example, given responses about how Target compares to Walmart, themes like Customer Support, Variety, and Clean Stores might emerge. The goal is to group responses into meaningful themes while maintaining a balance between generalization and specificity.

Additionally, sentiment analysis can be applied to themes (e.g., Customer Service (Positive) vs. Customer Service (Negative)).

## Approach

TODO

## Next steps

TODO
