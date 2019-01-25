# Reference

## Command line usage

### Overview

```
Usage: boca [OPTIONS] COMMAND [ARGS]...

Options:
  -v, -V, --version  Show the version and exit.
  --help             Show this message and exit.

Commands:
  init:custom  Generate files required to build custom commands.
  version      Show the version and exit.
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

Show the version and exit.
```
Usage: boca version [OPTIONS]

  Show the version and exit.

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
###  boca.version



####  Version


```python
Version(self, /, *args, **kwargs)
```
Version(boca, bocadillo)
####  get


```python
get() -> boca.version.Version
```
Retrieve the application versions.

__Returns__

`versions (Versions)`:
    Versions available at `versions.bocadillo` and `versions.boca`.

__Raises__

- `ModuleNotFoundError`: if Bocadillo is not installed.

####  version_option


```python
version_option(*idens, **attrs)
```
Add a version option to the CLI.

Immediately ends the program printing out the version number.

Inspired from `click.version_option`.

__Parameters__

- __*idens (str)__: identifiers for the option. Defaults to `"--version"`.

