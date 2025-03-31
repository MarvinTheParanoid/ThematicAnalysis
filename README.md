# Thematic Analysis

This project is a simple application aimed at extracting themes from text data. It focuses on analyzing open-text responses to identify recurring themes and patterns. It's still a work in progress and not fully operational yet.

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

You are given a dataset (walmart.csv) containing three columns of open-text responses. The task is to perform thematic analysis (also known as "theme counting") by identifying recurring themes within one or all of these columns.

For example, given responses about how Target compares to Walmart, themes like Customer Support, Variety, and Clean Stores might emerge. The goal is to group responses into meaningful themes while maintaining a balance between generalization and specificity.

Additionally, sentiment analysis can be applied to themes (e.g., Customer Service (Positive) vs. Customer Service (Negative)).

## Approach

I approached this problem in 3 main ways:

- **Single Prompt**: This method works well, which is not surprising given that it's essentially a summarization problem. It leverages the strengths of language models in condensing information into coherent themes. This still needs some iteration, and some changes to help it work with larger datasets.

- **Coding**: This approach was inspired by a challenge article. This approach worked reasonably well, and has some benefits over the single prompt approach, but I think there is a lot of improvements required. This approach could benefit from a reasoning model to improve consistency. Note, the API still needs updates based on insights from the coding notebook

- **Clustering**: Initially considered as I have fond memories of doing clustering at university, but I don't think it's a good fit for this problem. I started a quick test out of curiosity but didn't pursue it further.

### Other Approaches

- **Agent/Graph Approach**: An agent could focus on extracting a single, distinct theme, running in a loop until no more themes are found. This could be done with a map-reduce type approach, applying logic to batches of responses and then combining these into distinct themes.

- **Response IDs**: It would be useful to return IDs for responses strongly related to a theme, aiding UI and performance testing.
  A couple of ways I could think of doing this:

  1. **Vector/Similarity Search**: Using similarity search between embedded themes and responses could enhance theme extraction. This could be a step after any theme extraction strategy.
  1. **Tagging Rows**: LLMs could tag small batches of rows related to themes, working alongside similarity searches.

- **General Summarization**: Summarizing responses first, then generating themes, could leverage existing summarization models. This approach is more common and has a lot of overlap with thematic analysis.

## Improvements

- Add tests and proper documentation once the approach is finalized. It's a bit of cowboy repo at the moment, sorry,
- Explore using AI libraries. Pydantic AI is one I want to try out.
- Test different models, especially reasoning models.
- Implement a UI for drag-and-drop file uploads that lets users annotate the column types.
- Use the demographic columns to show themes by segments and do other interesting things.
- Create test cases and evaluate LLM response performance using LLMs (evals?)
- Re-architect to handle large datasets.

## Final Thoughts

Overall I'm not happy with where I got to, and I haven't yet found an approach I think would work really well.
In saying that, I had a lot of fun. I enjoy these kind of challenges, where there are multiple viable approaches and room for creativity.

When I get more time, and assuming nothing else takes my interest, I plan to coming back to this and iterate until I'm proud of it.
