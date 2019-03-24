# Custom commands

If you find yourself repeating certain tasks, you can automate them very easily via custom Queso commands.

## How custom commands are discovered

By default, Queso looks for custom commands in a `queso.py` script relative to the current working directory, as shown in the following example project structure:

```
.
├── app.py
└── queso.py
```

Every `queso.Command` declared in the custom commands script is mounted onto the root Queso command.

For example, the following `queso.py` script:

```python
# queso.py
import queso
import click

@queso.command()
def hello():
    """Show a warm welcome message."""
    click.echo("Hello, world!")
```

would allow to use the `hello` command like so:

```
$ queso hello
Hello, world!
```

:tada:

You can use all other Click's features (options, arguments, etc.) to build beautiful commands. See also the official [Click documentation][click-docs].

[click-docs]: https://click.palletsprojects.com

::: tip Q&A

**Why `@queso.command()` instead `@click.command()`?**

`@queso.command()` exists to prevent Queso from accidentally mounting non-Queso commands, e.g. Click commands that were simply imported into the custom commands script. You must use it or Queso won't be able to mount your custom commands.

**So do I have to use `@queso.group()` instead of `@click.group()`?**

Absolutely!

**How about `@click.option()`, `@click.argument()`, …?**

Use them as usual! We don't override any other Click feature. ;-)

:::

## Specifying the custom commands location

You can customize which file is used to discover custom commands using the `QUESO_COMMANDS` environment variable. It supports both absolute and relative paths.

```bash
export QUESO_COMMANDS=path/to/my_queso_commands.py
```
