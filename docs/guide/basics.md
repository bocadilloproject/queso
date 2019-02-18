# Basics

## Command line usage

Queso being a CLI application, it is first and foremost made to be used in the command line.

When it is installed, Queso makes itself available in the `PATH` as `queso`. You can invoke this executable to execute commands.

The usage is: `queso <COMMAND> [OPTIONS]`.

If you're ever unsure about a command, you can ask for `--help`:

```bash
$ queso version --help
Usage: queso version [OPTIONS]

  Show version information and exit.

Options:
  --help  Show this message and exit.
```

## Available commands

Queso ships with a certain number of built-in commands, which you can read more about in the [Built-in commands reference][built-in-commands].

```bash
$ queso
Usage: queso [OPTIONS] COMMAND [ARGS]...

Options:
  -v, -V, --version  Show the version and exit.
  --help             Show this message and exit.

Commands:
  init:custom  Generate files required to build custom commands.
  version      Show version information and exit.
```

An important feature of Queso is being very easy to extend. You can write your custom commands and use them just like the built-ins. You can read more about custom commands in the next section.

[built-in-commands]: ../reference/README.md#built-in-commands
