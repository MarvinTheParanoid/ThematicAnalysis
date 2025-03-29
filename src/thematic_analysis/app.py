from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Theme(BaseModel):
    name: str
    summary: str

class RequestModel(BaseModel):
    question: str
    answers: List[str]

class ResponseModel(BaseModel):
    themes: List[Theme]

@app.post("/get-themes", response_model=ResponseModel)
async def get_themes(request: RequestModel):
    return ResponseModel(themes=[Theme(name="Mock Theme", summary="This is a mock theme summary.")])
