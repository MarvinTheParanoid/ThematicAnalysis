from enum import StrEnum
from functools import partial
from typing import TypeAlias, TypeVar, Union

from openai.types.chat.chat_completion_system_message_param import (
    ChatCompletionSystemMessageParam,
)
from openai.types.chat.chat_completion_user_message_param import (
    ChatCompletionUserMessageParam,
)
from pydantic import BaseModel

RT = TypeVar("RT", bound=BaseModel)


class ThemeStrategy(StrEnum):
    """
    The strategy to use for the thematic analysis.
    """

    PROMPT = "prompt"


# This is a bit yuck, but cleans up the typing and makes it easier to work with
UserMessage = partial(ChatCompletionUserMessageParam, role="user")
SystemMessage = partial(ChatCompletionSystemMessageParam, role="system")
ChatCompletionMessage: TypeAlias = Union[
    ChatCompletionUserMessageParam, ChatCompletionSystemMessageParam
]
