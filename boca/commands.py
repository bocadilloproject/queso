import click

from .version import get_version

VERSION_KWARGS = {"prog_name": "Bocadillo", "message": "%(prog)s v%(version)s"}
VERSION_FLAGS = ("-v", "-V", "--version")


@click.command()
def version():
    """Show the version and exit."""
    click.echo(
        VERSION_KWARGS["message"]
        % {"prog": VERSION_KWARGS["prog_name"], "version": get_version()}
    )
