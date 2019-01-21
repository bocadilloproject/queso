import sys
import platform
from collections import namedtuple

from importlib import import_module
import click

__version__ = "0.0.1"

Versions = namedtuple("Version", "boca bocadillo")


def get() -> Versions:
    """Retrieve the application versions.

    # Returns
    versions (Versions):
        Versions available at `versions.bocadillo` and `versions.boca`.

    # Raises
    ModuleNotFoundError: if Bocadillo is not installed.
    """
    import bocadillo

    if get.simulate_module_not_found:
        raise ModuleNotFoundError("bocadillo")

    return Versions(boca=__version__, bocadillo=bocadillo.__version__)


# for testing
get.simulate_module_not_found = False


@click.command()
@click.pass_context
def show(ctx):
    """Show the Bocadillo and Boca versions."""
    try:
        versions = get()
    except ModuleNotFoundError:
        error = "Could not import bocadillo."
        hint = (
            "Are you sure it is installed "
            "and available on your PYTHONPATH environment variable? "
            "Did you forget to activate a virtual environment?"
        )
        click.echo(click.style(error, fg="red"), err=True)
        click.echo(click.style(hint, fg="yellow"))
        ctx.exit(1)
    else:
        items = (
            ("Boca", versions.boca),
            ("Bocadillo", versions.bocadillo),
            ("Python", ".".join(map(str, sys.version_info[:3]))),
            ("OS", platform.platform()),
        )
        click.echo("\n".join((f"{name}: {value}" for name, value in items)))
        ctx.exit()


def version_option(*idens, **attrs):
    """Add a version option to the CLI.
    
    Immediately ends the program printing out the version number.

    Inspired from `click.version_option`.

    # Parameters
    *idens (str): identifiers for the option. Defaults to `"--version"`.
    """

    def decorator(f):
        attrs.setdefault("is_flag", True)
        attrs.setdefault("expose_value", False)
        attrs.setdefault("is_eager", True)
        attrs.setdefault("help", "Show the version and exit.")

        def callback(ctx, param, value):
            if not value or ctx.resilient_parsing:
                return
            ctx.invoke(show)

        attrs["callback"] = callback
        return click.option(*(idens or ("--version",)), **attrs)(f)

    return decorator
