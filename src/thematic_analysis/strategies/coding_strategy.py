from thematic_analysis.llm import get_chat_completion_structured
from thematic_analysis.logger import get_logger
from thematic_analysis.models import (
    GroupedCodes,
    InitialCodes,
    ThemeRequest,
    ThemeResponse,
)
from thematic_analysis.prompts import (
    prompt_formatted_inputs,
    prompt_group_codes_instructions,
    prompt_initial_codes_instructions,
    prompt_themes_from_code_groups_instructions,
)
from thematic_analysis.types import SystemMessage, UserMessage
from thematic_analysis.utils.cleaning import (
    clean_answers,
    format_list,
    theme_request_to_polars,
)

logger = get_logger()


async def analyze_themes_with_coding(request: ThemeRequest) -> ThemeResponse:
    """
    Analyze the themes of a ThemeRequest using a single prompt step.
    """
    answers_df = theme_request_to_polars(request)
    cleaned_answers_df = clean_answers(answers_df)
    formatted_answers = format_list(cleaned_answers_df["answer"])

    initial_codes = await generate_initial_codes(formatted_answers)
    grouped_codes = await create_code_groups(initial_codes)
    themes = await generate_themes_from_code_groups(grouped_codes)
    return themes


# TODO: test if performance is better when less answers are used
# This functionality will need to be implemented anyway as the current approach will
# run out of context window for the LLM if too many answers are used
async def generate_initial_codes(formatted_answers: str) -> InitialCodes:
    """
    Generate initial codes for the answers.
    """
    prompts = [
        SystemMessage(
            content=prompt_initial_codes_instructions,
        ),
        UserMessage(
            content=prompt_formatted_inputs.format(formatted_answers=formatted_answers)
        ),
    ]
    return await get_chat_completion_structured(
        prompts=prompts,
        response_schema=InitialCodes,
    )


async def create_code_groups(initial_codes: InitialCodes) -> GroupedCodes:
    """
    Create code groups from the initial codes.
    """
    # TODO: fix this naming... it's not easy to reason about...
    all_codes = [code for codes in initial_codes.codes for code in codes.codes]
    formatted_codes = format_list(all_codes)

    prompts = [
        SystemMessage(
            content=prompt_group_codes_instructions,
        ),
        UserMessage(
            content=prompt_formatted_inputs.format(formatted_answers=formatted_codes),
        ),
    ]
    return await get_chat_completion_structured(
        prompts=prompts,
        response_schema=GroupedCodes,
    )


async def generate_themes_from_code_groups(
    grouped_codes: GroupedCodes,
) -> ThemeResponse:
    """
    Generate themes from the code groups.
    """
    # Format will be a code group per line, with each code group formatted as follows:
    # ("code 1", "code 2", "code 3")
    formatted_code_groups = format_list(
        [
            f"({', '.join(format_list(codes.codes, delimiter=', '))})"
            for codes in grouped_codes.codes
        ],
    )

    prompts = [
        SystemMessage(
            content=prompt_themes_from_code_groups_instructions,
        ),
        UserMessage(
            content=prompt_formatted_inputs.format(
                formatted_answers=formatted_code_groups
            ),
        ),
    ]
    return await get_chat_completion_structured(
        prompts=prompts,
        response_schema=ThemeResponse,
    )
