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

Queso ships with a certain number of **built-in commands**, which you can read more about in the [API reference](/reference/).

You can also write your **custom commands** and use them just like the built-in ones. Read more about this in the next section!
