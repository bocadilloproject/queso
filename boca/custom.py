import os

from .groups import FileGroup

CUSTOM_COMMANDS_ENV_VAR = "BOCA_CUSTOM_COMMANDS"


def get_custom_commands_path():
    return os.getenv(CUSTOM_COMMANDS_ENV_VAR, "boca.py")


class CustomCommandsGroup(FileGroup):
    def __init__(self, *args, **kwargs):
        super().__init__(get_custom_commands_path(), *args, **kwargs)
