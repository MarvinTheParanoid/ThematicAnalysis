from thematic_analysis.llm import get_chat_completion_structured
from thematic_analysis.models import ThemeRequest, ThemeResponse
from thematic_analysis.prompts import (
    prompt_formatted_inputs,
    prompt_strategy_instructions,
)
from thematic_analysis.types import SystemMessage, UserMessage
from thematic_analysis.utils.cleaning import (
    clean_answers,
    format_list,
    theme_request_to_polars,
)


async def analyze_themes_with_prompt(request: ThemeRequest) -> ThemeResponse:
    """
    Analyze the themes of a ThemeRequest using a single prompt step.
    """
    answers_df = theme_request_to_polars(request)
    cleaned_answers_df = clean_answers(answers_df)
    formatted_answers = format_list(cleaned_answers_df["answer"])
    prompts = [
        SystemMessage(
            content=prompt_strategy_instructions,
        ),
        UserMessage(
            content=prompt_formatted_inputs.format(formatted_answers=formatted_answers),
        ),
    ]
    return await get_chat_completion_structured(
        prompts=prompts,
        response_schema=ThemeResponse,
    )
