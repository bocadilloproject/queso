import click

from . import commands
from .options import version_option
from queso.commands import CustomCommandsGroup


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
        if not isinstance(value, commands.QuesoCommand):
            continue
        if getattr(value, "__queso_ignore__", None):
            continue
        cli.add_command(value)

    return cli
