import os

from .constants import CUSTOM_COMMANDS_ENV_VAR, DEFAULT_CUSTOM_COMMANDS
from .groups import FileGroup


def get_custom_commands_path() -> str:
    return os.getenv(CUSTOM_COMMANDS_ENV_VAR, DEFAULT_CUSTOM_COMMANDS)


class CustomCommandsGroup(FileGroup):
    def __init__(self, *args, **kwargs):
        super().__init__(get_custom_commands_path(), *args, **kwargs)
