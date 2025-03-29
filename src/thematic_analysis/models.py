from typing import List

from pydantic import BaseModel, Field, field_validator

from thematic_analysis.types import ThemeStrategy


class Theme(BaseModel):
    """
    Represents a theme found in the answers.
    """

    name: str = Field(..., description="The name of the theme.")
    summary: str = Field(..., description="A summary of the theme.")


class ThemeRequest(BaseModel):
    """
    Represents a request to the thematic analysis API.
    """

    question: str = Field(..., description="The question to analyze.")
    answers: List[str] = Field(
        ...,
        description="The answers to analyze.",
        min_length=1,
    )
    ids: List[str] = Field(
        ...,
        description="The ids of the answers.",
        min_length=1,
    )

    strategy: ThemeStrategy = Field(
        ThemeStrategy.PROMPT, description="The strategy to use for the analysis."
    )

    @field_validator("ids", "answers")
    def validate_ids(cls, v, values):
        """
        Check that the ids are unique and have the same length as the answers.
        """
        if len(set(v)) != len(v):
            raise ValueError("ids must be unique")
        if len(v) != len(values["answers"]):
            raise ValueError("answers and ids must have the same length")
        return v


class ThemeResponse(BaseModel):
    """
    Represents a response from the thematic analysis API.
    """

    themes: List[Theme] = Field(..., description="The themes found in the answers.")
