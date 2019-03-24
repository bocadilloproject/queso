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


def get_versions() -> Versions:
    """Retrieve versions for Queso, Bocadillo.

    # Returns
    versions (Versions):
        An object containing the `bocadillo` and `queso` version as eponymous
        attributes.
    """
    try:
        import bocadillo

        if get_versions.simulate_module_not_found:
            raise ImportError("bocadillo")
    except ImportError:
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
get_versions.simulate_module_not_found = False
