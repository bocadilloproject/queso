from contextlib import redirect_stdout, suppress
import traceback
from io import StringIO
from typing import NamedTuple, Any

import click

from .cli import create_cli


class CommandResult(NamedTuple):
    exit_code: int
    value: Any
    output: str


def call_command(
    name: str,
    *args: str,
    capture_errors: bool = False,
    cli: click.Command = None
) -> CommandResult:
    """Call a command programmatically.

    Any output made by the command is captured and included in the result.
    
    Exit code is `0` if the command exits successfully (regardless of its return value), or `1` if a non-Click exception occurs. For other situations, the original Click behavior is honored.

    # Parameters
    name (str):
        The name of the command to call, e.g. `"version"`.
    *args (str):
        A series of command line parameters to be parsed.
    capture_errors (bool):
        `True`, Click exceptions are silenced and written to the captured stdout. Note that other exceptions will still propagate. Defaults to `False`.
    cli (click.Command):
        The Click CLI application instance to use. Defaults to `create_cli()`.

    # Returns
    result (CommandResult):
        Holds the `exit_code` (int), its return `value`,
        and the captured `output` (str).

    # Example

    ```python
    >>> from boca import call_command
    >>> r = call_command("version", "--help")
    >>> r.exit_code
    0
    ```
    """
    if cli is None:
        cli = create_cli()

    args = (name, *args)

    # Defaults.
    value = None
    exit_code = 0

    with redirect_stdout(StringIO()) as output:
        try:
            # pylint: disable=too-many-function-args, unexpected-keyword-arg
            value = cli(args, prog_name=cli.name, standalone_mode=False)
        except click.ClickException as exc:
            exit_code = exc.exit_code
            if capture_errors is True:
                exc.show(file=output)
            else:
                raise
        except BaseException as exc:
            exit_code = 2
            if capture_errors is all:
                traceback.print_exc(file=output)
            else:
                raise

    return CommandResult(
        value=value, exit_code=exit_code, output=output.getvalue()
    )
