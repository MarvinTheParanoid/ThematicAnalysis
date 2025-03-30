from typing import List, Union

from pydantic import BaseModel, Field, field_validator

from thematic_analysis.types import ThemeStrategy


class SurveyAnswer(BaseModel):
    """
    Represents an answer to a survey question.
    """

    id: str = Field(..., description="The id of the answer.")
    answer: Union[str, None] = Field(..., description="The answer to the question.")


class ThemeRequest(BaseModel):
    """
    Represents a request to the thematic analysis API.
    """

    question: str = Field(..., description="The question to analyze.")
    answers: List[SurveyAnswer] = Field(
        ...,
        description="The answers to analyze.",
        min_length=1,
    )

    strategy: ThemeStrategy = Field(
        ThemeStrategy.PROMPT, description="The strategy to use for the analysis."
    )

    @field_validator("answers")
    def validate_ids(cls, v, values):
        """
        Check that the ids are unique.
        """
        ids = [answer.id for answer in v]
        if len(set(ids)) != len(ids):
            raise ValueError("ids must be unique")
        return v


class Theme(BaseModel):
    """
    Represents a theme found in the answers.
    """

    name: str = Field(..., description="The name of the theme.")
    summary: str = Field(..., description="A summary of the theme.")

    @property
    def markdown(self) -> str:
        """
        Returns the theme as a markdown string.
        """
        return f"**{self.name}**\n\n{self.summary}"


class ThemeResponse(BaseModel):
    """
    Represents a response from the thematic analysis API.
    """

    themes: List[Theme] = Field(..., description="The themes found in the answers.")


class Codes(BaseModel):
    """
    Represents a list of codes for a single answer.
    """

    codes: List[str] = Field(..., description="A list of codes")


class InitialCodes(BaseModel):
    """
    Represents a list of codes for a survey.
    """

    codes: List[Codes] = Field(..., description="A list of codes for each answer.")


class GroupedCodes(BaseModel):
    """
    Represents a list of grouped codes for a survey.
    """

    codes: List[Codes] = Field(..., description="A list of grouped codes.")
