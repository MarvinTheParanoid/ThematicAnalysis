from fastapi import APIRouter

from thematic_analysis.models import Theme, ThemeRequest, ThemeResponse

router = APIRouter(prefix="/themes", tags=["themes"])


@router.post("/analyze", response_model=ThemeResponse)
async def analyze_themes(request: ThemeRequest):
    return ThemeResponse(
        themes=[Theme(name="Mock Theme", summary="This is a mock theme summary.")]
    )
