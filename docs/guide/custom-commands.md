# Custom commands

If you find yourself repeating certain tasks, you can automate them very easily via custom Boca commands.

## How custom commands are discovered

Boca looks for custom commands in a `boca.py` script relative to the current working directory, as shown in the following example project structure:

```
.
├── api.py
└── boca.py
```

Every `click.Command` object present in this file is mounted onto the root Boca command. For example, a custom `hello` command would be made available as `$ boca hello`.

::: tip
You can customize which file is used for command discovery using the `BOCA_CUSTOM_COMMANDS` environment variable. It supports both absolute and relative paths.
:::

## Example

Let's create a `boca.py` file at the root of our project directory and use Click to declare a simple `hello` command:

```python
# boca.py
import click

@click.command()
def hello():
    """Show a warm welcome message."""
    click.echo("Hello, world!")
```

Once this is done, we're ready to use the `hello` command through Boca:

```
$ boca hello
Hello, world!
```

:tada:

From here, the whole world of Click is open to us. For example, let's show the generated usage tips for our newly declared command:

```
$ boca hello --help
Usage: boca hello [OPTIONS]

  Show a warm welcome message.

Options:
  --help  Show this message and exit.
```

You can make use of any Click feature to build commands that help you automate certain tasks. See also the official [Click documentation][click-docs].

[click-docs]: https://click.palletsprojects.com
