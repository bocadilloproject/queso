# Guide

[[toc]]

## Introduction

Queso is the official development toolkit for building applications with [Bocadillo](https://bocadilloproject.github.io).

Features include:

- Zero-configuration: Once installed, you can run and extend Queso out of the box.
- Extensibility: automate common tasks with custom commands.
- Familiarity: Queso is built on top of [Click](http://click.palletsprojects.com). Anything you can do with Click, you can do with Queso.

::: tip CONTRIBUTING
We're constantly working towards bringing more awesome commands to Queso.

Have an idea about a super-useful command that should be included? Go ahead and [open a feature request](https://github.com/bocadilloproject/queso/issues/new) on GitHub!
:::

## Installation

::: warning REQUIREMENTS
Queso is compatible with **Python 3.6+**.
:::

1. Install Queso using `pip`:

```bash
pip install queso
```

2. Try it out:

```bash
$ queso -V
Queso: 0.2.1
Bocadillo: 0.13.1
Python: 3.7.2
OS: Darwin-18.2.0-x86_64-i386-64bit
```

Note: you may have another OS or a different version of Queso, Bocadillo, or Python installed.

Although Queso was made to work hand in hand with [Bocadillo](https://bocadilloproject.github.io), you'll need to install Bocadillo separately. Some commands will not work if you don't have Bocadillo installed.

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
