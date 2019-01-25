import platform
import sys
from typing import NamedTuple

import click

__version__ = "0.0.1"


class Versions(NamedTuple):

    boca: str
    bocadillo: str
    python: str
    os: str

    def __str__(self):
        items = (
            ("Boca", self.boca),
            ("Bocadillo", self.bocadillo),
            ("Python", self.python),
            ("OS", self.os),
        )
        return "\n".join((f"{name}: {value}" for name, value in items))


def get() -> Versions:
    """Retrieve versions for Boca, Bocadillo.

    # Returns
    versions (Versions):
        An object containing the `bocadillo` and `boca` version as eponymous
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
        boca=__version__,
        bocadillo=bocadillo_version,
        python=".".join(map(str, sys.version_info[:3])),
        os=platform.platform(),
    )


# for testing
get.simulate_module_not_found = False


@click.command()
@click.pass_context
def show(ctx):
    """Show the Bocadillo and Boca versions."""
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
