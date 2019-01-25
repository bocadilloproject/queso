# Changelog

All notable changes to Boca are documented here.

The format of this document is based on [Keep a Changelog](https://keepachangelog.com).

**Versioning policy**

Boca adheres to [Semantic Versioning](https://semver.org).

## [Unreleased]

## [v0.1.0] - 2019-01-25

This release focuses on reimplementing the behavior of the CLI built into the `bocadillo` package as of v0.10.1, with some additions and slight changes.

### Added

- `version` command, also accessible using `-v`, `-V` and `--version` flags.
- `init:custom` command.
- Programmatic usage using the `call_command()` helper.
- Documentation site.

### Changed

Relative to Bocadillo v0.10.1:

- Custom commands:
    - It is not mendatory anymore to declare a `click.Group` in the custom commands file. All `click.Command` objects declared in the file are mounted onto `boca`. This includes commands declared with `@click.command()`, groups declared with `@click.group()` and any other instance of a subclass of `click.Command`.
    - **BREAKING**: The environment variable changed from `BOCA_CUSTOM_COMMANDS_FILE` to `BOCA_CUSTOM_COMMANDS`.

## v0.0.1 - 2019-01-20

Initial release to PyPI.

[Unreleased]: https://github.com/bocadilloproject/boca/compare/v0.1.0...HEAD
[v0.1.0]: https://github.com/bocadilloproject/boca/compare/v0.0.1...v0.1.0
