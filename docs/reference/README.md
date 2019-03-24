# Reference

This document describes all public commands, functions, classes and modules in Queso.
## Command line usage

### Overview

```
Usage: queso [OPTIONS]

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
Usage: queso init:custom [OPTIONS]

  Generate files required to build custom commands.

Options:
  -d, --directory TEXT  Where files should be generated.
  --help                Show this message and exit.
```

#### version

Show version information and exit.
```
Usage: queso version [OPTIONS]

  Show version information and exit.

Options:
  --help  Show this message and exit.
```

## Python modules

###  queso.cli



####  create_cli


```python
create_cli() -> click.core.Command
```
Build and return an instance of `queso`.

__Returns__

`cli (click.Command)`: contains both built-in and custom commands.

###  queso.commands



####  QuesoCommand


```python
QuesoCommand(self, name, context_settings=None, callback=None, params=None, help=None, epilog=None, short_help=None, options_metavar='[OPTIONS]', add_help_option=True, hidden=False, deprecated=False)
```
Base class for Queso commands.

Merely a subclass of [click.Command][clickcommand].

[clickcommand]: http://click.palletsprojects.com/en/7.x/api/#click.Command

####  QuesoGroup


```python
QuesoGroup(self, name=None, commands=None, **attrs)
```
Base class for Queso command groups.

A subclass of [QuesoCommand](#quesocommand) and [click.Group][clickgroup].

[clickgroup]: http://click.palletsprojects.com/en/7.x/api/#click.Group

####  FileGroup


```python
FileGroup(self, path: str, *args, **kwargs)
```
A [QuesoGroup](#quesogroup) that loads commands declared in a file.

__Parameters__

- __path (str)__:
    path to a Python module that contains Click commands
    (declared with `@click.command()` or `@click.group()`).

####  CustomCommandsGroup


```python
CustomCommandsGroup(self, *args, **kwargs)
```
A [FileGroup](#filegroup) that loads custom commands.

The custom commands file is `./queso.py` by default. This can be
overridden by setting the `QUESO_COMMANDS` environment variable.

###  queso.utils



####  call_command


```python
call_command(name: str, *args: str, capture_errors: bool = False, cli: click.core.Command = None) -> queso.utils.CommandResult
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
>>> from queso import call_command
>>> r = call_command("version", "--help")
>>> r.exit_code
0
```

