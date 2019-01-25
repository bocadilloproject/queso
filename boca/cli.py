import click

from . import commands
from .custom import CustomCommandsGroup
from .versions import version_option


def create_cli() -> click.Command:
    """This is the Bocadillo CLI factory.

    ::: tip
    Use this function to obtain an instance of `boca` for programmatic use.
    :::

    # Returns
    cli (click.Command): an instance of the `boca` CLI.
    """

    @click.group(name="boca", cls=CustomCommandsGroup)
    @version_option("-v", "-V", "--version")
    def cli():
        pass

    for value in vars(commands).values():
        if isinstance(value, click.Command):
            cli.add_command(value)

    return cli
