import os

import click

from . import scaffold
from .versions import get as get_versions
from .custom import get_custom_commands_path


@click.command()
def version():
    """Show version information and exit."""
    versions = get_versions()
    click.echo(str(versions))


@click.command(name="init:custom")
@click.option(
    "-d", "--directory", default="", help="Where files should be generated."
)
def init_custom(directory: str):
    """Generate files required to build custom commands."""
    dest = os.path.join(directory, get_custom_commands_path())
    scaffold.copy("queso.py", dest)
    click.echo(click.style(f"Generated {dest}", fg="green"))
    click.echo("Open the file and start building!")
