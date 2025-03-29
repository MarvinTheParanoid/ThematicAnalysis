from typing import List

from pydantic import BaseModel


class Theme(BaseModel):
    name: str
    summary: str


class ThemeRequest(BaseModel):
    question: str
    answers: List[str]


class ThemeResponse(BaseModel):
    themes: List[Theme]
