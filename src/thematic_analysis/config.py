from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # TODO: rethink this - we might want to use different models for different tasks
    openai_completion_model: str = Field(
        default="gpt-4o-mini",
        description="The OpenAI model to use for the thematic analysis",
    )
    openai_embedding_model: str = Field(
        default="text-embedding-3-small",
        description="The OpenAI model to use for the embedding",
    )
    openai_api_key: str = Field(
        ...,
        description="The OpenAI API key",
    )

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()  # type: ignore
