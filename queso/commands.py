import os

import click
import runpy


__all__ = ["command", "group", "QuesoCommand", "QuesoGroup"]


class QuesoCommand(click.Command):
    """Base class for Queso commands.

    Merely a subclass of [click.Command][clickcommand].

    [clickcommand]: http://click.palletsprojects.com/en/7.x/api/#click.Command
    """

    include_options_metavar = True

    def collect_usage_pieces(self, ctx):
        rv = [self.options_metavar] if self.include_options_metavar else []
        for param in self.get_params(ctx):
            if param.nargs == -1:
                rv.append("--")
            rv.extend(param.get_usage_pieces(ctx))
        return rv


class QuesoGroup(QuesoCommand, click.Group):
    """Base class for Queso command groups.

    A subclass of [QuesoCommand](#quesocommand) and [click.Group][clickgroup].

    [clickgroup]: http://click.palletsprojects.com/en/7.x/api/#click.Group
    """


class FileGroup(QuesoGroup):
    """A [QuesoGroup](#quesogroup) that loads commands declared in a file.

    # Parameters
    path (str):
        path to a Python module that contains Click commands
        (declared with `@click.command()` or `@click.group()`).
    """

    def __init__(self, path: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        try:
            namespace = runpy.run_path(path)
        except FileNotFoundError:
            # User did not create custom commands
            return
        else:
            for value in namespace.values():
                if isinstance(value, QuesoCommand):
                    self.add_command(value)


class CustomCommandsGroup(FileGroup):
    """A [FileGroup](#filegroup) that loads custom commands.

    The custom commands file is `./queso.py` by default. This can be
    overridden by setting the `QUESO_COMMANDS` environment variable.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(self.path(), *args, **kwargs)

    @staticmethod
    def path():
        return os.getenv("QUESO_COMMANDS", "queso.py")


def command(name: str = None, **kwargs) -> QuesoCommand:
    """Replacement for `click.command()` with `QuesoCommand` as a base class."""
    return click.command(name=name, cls=QuesoCommand, **kwargs)


def group(name: str = None, **kwargs) -> QuesoGroup:
    """Replacement for `click.group()` with `QuesoGroup` as a base class."""
    return click.group(name=name, cls=QuesoGroup, **kwargs)
