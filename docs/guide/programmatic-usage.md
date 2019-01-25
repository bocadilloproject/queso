# Programmatic usage

Boca ships with a `call_command` helper function which you can use if you need to call commands from your code.

## Basic usage

At the most basic level, `call_command` expects that you pass the name of the command first, and then any extra command line options to be parsed.

Here's an example that is equivalent to executing `$ boca version --help`:

```python
from boca import call_command

call_command("version", "--help")
```


## Command results

The `call_command` function returns a `CommandResult` object which contains valuable information about the execution of the command:

- `exit_code`: the command's exit code, e.g. `0` if all went well.
- `value`: the return value of the command callback, or `None`.
- `output`: a string containing the captured standard output.

## Error handling

By default, any exception that occurs during the execution of the command is propagated to the callee.

However, the `capture_errors` keyword argument can be used to capture exceptions:

- If set to `True`, Click exceptions such as `UsageError` or `Abort` will be captured and the `exit_code` will be set to that of the exception.
- If set to `all` (the built-in), any exception will be captured, and the `exit_code` will be set to 2 if it cannot be obtained from the exception.

### Examples

Let's declare in a [custom commands file][custom-commands] a command that fails with a `RuntimeError`:

```python
# boca.py
import click

@click.command()
def fail():
    raise RuntimeError("This is unexpected…")
```

Here are a few examples that demonstrate how error handling works:

- Exceptions are propagated by default:

```python
>>> call_command("foo")
[...] # Traceback truncated for brievety
click.exceptions.UsageError: No such command "foo".
```

```python
>>> call_command("fail")
[...] # Traceback truncated for brievety
RuntimeError: This is unexpected…
```

- Capture Click exceptions:

```python
    # Captures the `UsageError` raised when not finding a command.
>>> result = call_command("foo", capture_errors=True)
>>> result.exit_code
2
>>> print(result.output)
Usage: boca [OPTIONS] COMMAND [ARGS]...
Try "boca --help" for help.

Error: No such command "foo".
```

- Capture any exception:

```python
>>> result = call_command("fail", capture_errors=all)
>>> result.exit_code  # 2
>>> print(result.output)
```

[custom-commands]: ./custom-commands.md
