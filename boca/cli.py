import click

from .commands import version
from .custom import CustomCommandsGroup
from .version import get_version

VERSION_KWARGS = {"prog_name": "Bocadillo", "message": "%(prog)s v%(version)s"}
VERSION_FLAGS = ("-v", "-V", "--version")


def create_cli() -> click.Command:
    """This is the Bocadillo CLI factory.

    ::: tip
    Use this function to obtain an instance of `boca` for programmatic use.
    :::

    # Returns
    cli (click.Command): an instance of the `boca` CLI.
    """

    @click.group(cls=CustomCommandsGroup)
    @click.version_option(get_version(), *VERSION_FLAGS, **VERSION_KWARGS)
    def cli():
        pass

    cli.add_command(version)

    return cli
