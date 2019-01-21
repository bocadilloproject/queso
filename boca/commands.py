import os

import click

from . import scaffold, version as _version
from .custom import get_custom_commands_path


@click.command()
@click.pass_context
def version(ctx):
    """Show the version and exit."""
    ctx.forward(_version.show)


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
