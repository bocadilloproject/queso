import os

import click

from queso import scaffold
from queso.commands import CustomCommandsGroup, QuesoCommand
from queso.versions import get_versions


@click.command(cls=QuesoCommand)
def version():
    """Show version information and exit."""
    click.echo(str(get_versions()))


@click.command(name="init:custom", cls=QuesoCommand)
@click.option(
    "-d", "--directory", default="", help="Where files should be generated."
)
def init_custom(directory: str):
    """Generate files required to build custom commands."""
    dest = os.path.join(directory, CustomCommandsGroup.path())
    scaffold.copy("queso.py", dest)
    click.echo(click.style(f"Generated {dest}", fg="green"))
    click.echo("Open the file and start building!")
