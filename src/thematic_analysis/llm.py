from typing import List, Type, cast

from openai import AsyncOpenAI

from thematic_analysis.config import settings
from thematic_analysis.logger import get_logger
from thematic_analysis.types import RT, ChatCompletionMessage

logger = get_logger()


# TODO: create a singleton for the OpenAI client or some other method to ensure
# that the client is not created multiple times
def get_llm_client() -> AsyncOpenAI:
    """
    Get an OpenAI client.
    """
    logger.info("Getting OpenAI client")
    return AsyncOpenAI(api_key=settings.openai_api_key)


async def get_chat_completion(prompts: List[ChatCompletionMessage]) -> str:
    """
    Get a response from the LLM.
    """
    client = get_llm_client()
    # TODO: implement proper error handling for the OpenAI unhappy paths
    response = await client.chat.completions.create(
        model=settings.openai_completion_model,
        messages=prompts,
        temperature=0,
    )
    # TODO: add debug logging with info about the response, e.g. tokens used, etc.
    return cast(str, response.choices[0].message.content)


async def get_chat_completion_structured(
    prompts: List[ChatCompletionMessage],
    response_schema: Type[RT],
) -> RT:
    """
    Get a structured response from the LLM.
    """
    client = get_llm_client()
    # TODO: implement proper error handling for the OpenAI unhappy paths
    response = await client.beta.chat.completions.parse(
        model=settings.openai_completion_model,
        messages=prompts,
        response_format=response_schema,
        temperature=0,
    )
    return response_schema.model_validate(response.choices[0].message.parsed)


async def get_embeddings(text: List[str]) -> List[List[float]]:
    """
    Get an embedding for a text.
    """
    client = get_llm_client()
    response = await client.embeddings.create(
        input=text, model=settings.openai_embedding_model
    )
    return [embedding.embedding for embedding in response.data]
