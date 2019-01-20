import os

import click

from . import scaffold
from .version import get_version
from .custom import get_custom_commands_path

VERSION_KWARGS = {"prog_name": "Bocadillo", "message": "%(prog)s v%(version)s"}
VERSION_FLAGS = ("-v", "-V", "--version")


@click.command()
def version():
    """Show the version and exit."""
    click.echo(
        VERSION_KWARGS["message"]
        % {"prog": VERSION_KWARGS["prog_name"], "version": get_version()}
    )


@click.command(name="init:custom")
@click.option(
    "-d", "--directory", default="", help="Where files should be generated."
)
def init_custom(directory: str):
    """Generate files required to build custom commands."""
    dest = os.path.join(directory, get_custom_commands_path())
    scaffold.copy("boca.py", dest)
    click.echo(click.style(f"Generated {dest}", fg="green"))
    click.echo("Open the file and start building!")
