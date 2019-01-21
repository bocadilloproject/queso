# Changelog

All notable changes to Boca are documented here.

The format of this document is based on [Keep a Changelog](https://keepachangelog.com).

**Versioning policy**

Boca adheres to [Semantic Versioning](https://semver.org).

## [Unreleased]

### Added

- `version` command, also accessible using `-v`, `-V` and `--version` flags.
- `init:custom` command.
- Custom commands:
    - Loaded from the `BOCA_CUSTOM_COMMANDS` file, defaulting to `boca.py` in the current directory.
    - All `click.Command` objects declared in the file are mounted onto `boca`.
    This includes commands declared with `@click.command()`, groups declared
    with `@click.group()` and any other instance of a subclass of `click.Command`.

## v0.0.1 - 2018-01-20

Initial release to PyPI.

[Unreleased]: https://github.com/bocadilloproject/boca/compare/v0.0.1...HEAD
