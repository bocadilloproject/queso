import click

from queso.commands import Command, CustomCommandsGroup

from . import commands
from .options import version_option


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
        if not isinstance(value, Command):
            continue
        cli.add_command(value)

    return cli
