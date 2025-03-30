from fastapi import APIRouter, HTTPException

from thematic_analysis.logger import get_logger
from thematic_analysis.models import ThemeRequest, ThemeResponse
from thematic_analysis.strategies.prompt_strategy import analyze_themes_with_prompt
from thematic_analysis.types import ThemeStrategy

logger = get_logger()

router = APIRouter(prefix="/themes", tags=["themes"])


@router.post("/analyze", response_model=ThemeResponse)
async def analyze_themes(request: ThemeRequest):
    """
    Analyze the themes of the given request.
    """
    # TODO: convert the answer to polars and clean them
    match request.strategy:
        case ThemeStrategy.PROMPT:
            return await analyze_themes_with_prompt(request)
        case _:
            raise HTTPException(status_code=400, detail="Invalid strategy")
