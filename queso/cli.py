import click

from . import commands
from .custom import CustomCommandsGroup
from .versions import version_option


def create_cli() -> click.Command:
    """Build and return an instance of `queso`.

    # Returns
    cli (click.Command): contains both built-in and custom commands.
    """

    @click.group(name="queso", cls=CustomCommandsGroup)
    @version_option("-v", "-V", "--version")
    def cli():
        pass

    for value in vars(commands).values():
        if isinstance(value, click.Command):
            cli.add_command(value)

    return cli
