from typing import Iterable

import polars as pl

from thematic_analysis.models import SurveyAnswer, ThemeRequest


def theme_request_to_polars(request: ThemeRequest) -> pl.DataFrame:
    """
    Create a polars dataframe from the answers and ids of a ThemeRequest.
    """
    return pl.DataFrame([answer.model_dump() for answer in request.answers])


def clean_answers(answers: pl.DataFrame) -> pl.DataFrame:
    """
    Clean the answers of a ThemeRequest.

    This function cleans the whitespace and removes empty answers.
    """
    return (
        answers.with_columns(
            pl.col("answer")
            .str.strip_chars()
            .str.replace_all(r"\s+", " ")
            .alias("answer")
        )
        .filter(pl.col("answer").str.len_chars() > 0)
        .drop_nulls()
    )


def format_answers(answers: Iterable[str], delimiter: str = "\n") -> str:
    """
    Format the answers of a ThemeRequest for a prompt.
    """
    quoted_answers = [f'"{answer}"' for answer in answers]
    return delimiter.join(quoted_answers)
