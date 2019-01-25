# Basics

## Command line usage

Boca being a CLI application, it is first and foremost made to be used in the command line.

When it is installed, Boca makes itself available in the `PATH` as `boca`. You can invoke this executable to execute commands.

The usage is: `boca <COMMAND> [OPTIONS]`.

If you're ever unsure about a command, you can ask for `--help`:

```bash
$ boca version --help
Usage: boca version [OPTIONS]

  Show version information and exit.

Options:
  --help  Show this message and exit.
```

## Available commands

Boca ships with a certain number of built-in commands, which you can read more about in the [Built-in commands reference][built-in-commands].

```bash
$ boca
Usage: boca [OPTIONS] COMMAND [ARGS]...

Options:
  -v, -V, --version  Show the version and exit.
  --help             Show this message and exit.

Commands:
  init:custom  Generate files required to build custom commands.
  version      Show version information and exit.
```

An important feature of Boca is being very easy to extend. You can write your custom commands and use them just like the built-ins. You can read more about custom commands in the next section.

[built-in-commands]: ../reference/README.md#built-in-commands
