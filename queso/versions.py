import platform
import sys
from typing import NamedTuple

import click

__version__ = "0.2.0"


class Versions(NamedTuple):

    queso: str
    bocadillo: str
    python: str
    os: str

    def __str__(self):
        items = (
            ("Queso", self.queso, "yellow"),
            ("Bocadillo", self.bocadillo, "green"),
            ("Python", self.python, None),
            ("OS", self.os, None),
        )
        return "\n".join(
            f"{click.style(name, bold=True, fg=fg)}: {value}"
            for name, value, fg in items
        )


def get() -> Versions:
    """Retrieve versions for Queso, Bocadillo.

    # Returns
    versions (Versions):
        An object containing the `bocadillo` and `queso` version as eponymous
        attributes.
    """
    try:
        import bocadillo

        if get.simulate_module_not_found:
            raise ModuleNotFoundError("bocadillo")
    except ModuleNotFoundError:
        bocadillo_version = "[Not installed]"
    else:
        bocadillo_version = bocadillo.__version__

    return Versions(
        queso=__version__,
        bocadillo=bocadillo_version,
        python=".".join(map(str, sys.version_info[:3])),
        os=platform.platform(),
    )


# for testing
get.simulate_module_not_found = False


@click.command()
@click.pass_context
def show(ctx):
    """Show the Bocadillo and Queso versions."""
    versions = get()
    click.echo(str(versions))
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
