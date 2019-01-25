# Reference

This document describes all public commands, functions, classes and modules in Boca.
## Command line usage

### Overview

```
Usage: boca [OPTIONS] COMMAND [ARGS]...

Options:
  -v, -V, --version  Show the version and exit.
  --help             Show this message and exit.

Commands:
  init:custom  Generate files required to build custom commands.
  version      Show version information and exit.
```

### Built-in commands

#### init:custom

Generate files required to build custom commands.
```
Usage: boca init:custom [OPTIONS]

  Generate files required to build custom commands.

Options:
  -d, --directory TEXT  Where files should be generated.
  --help                Show this message and exit.
```

#### version

Show version information and exit.
```
Usage: boca version [OPTIONS]

  Show version information and exit.

Options:
  --help  Show this message and exit.
```

## Python modules

###  boca.cli



####  create_cli


```python
create_cli() -> click.core.Command
```
This is the Bocadillo CLI factory.

::: tip
Use this function to obtain an instance of `boca` for programmatic use.
:::

__Returns__

`cli (click.Command)`: an instance of the `boca` CLI.

###  boca.constants


This module contains various useful constants, listed below.
```python
CUSTOM_COMMANDS_ENV_VAR = "BOCA_CUSTOM_COMMANDS"
DEFAULT_CUSTOM_COMMANDS = "boca.py"
```
###  boca.utils



####  CommandResult


```python
CommandResult(self, /, *args, **kwargs)
```
CommandResult(exit_code, value, output)
####  call_command


```python
call_command(name: str, *args: str, capture_errors: bool = False, cli: click.core.Command = None) -> boca.utils.CommandResult
```
Call a command programmatically.

Any output made by the command is captured and included in the result.

Exit code is `0` if the command exits successfully (regardless of its return value), or `1` if a non-Click exception occurs. For other situations, the original Click behavior is honored.

__Parameters__

- __name (str)__:
    The name of the command to call, e.g. `"version"`.
- __*args (str)__:
    A series of command line parameters to be parsed.
- __capture_errors (bool)__:
    `True`, Click exceptions are silenced and written to the captured stdout. Note that other exceptions will still propagate. Defaults to `False`.
- __cli (click.Command)__:
    The Click CLI application instance to use. Defaults to `create_cli()`.

__Returns__

`result (CommandResult)`:
    Holds the `exit_code` (int), its return `value`,
    and the captured `output` (str).

__Example__


```python
>>> from boca import call_command
>>> r = call_command("version", "--help")
>>> r.exit_code
0
```

