import os
from typing import Any, Callable, List, TypeVar

import click
import runpy


__all__ = ["command", "group", "Command", "Group"]


class Command(click.Command):
    """Base class for Queso commands.

    Merely a subclass of [click.Command][clickcommand].

    [clickcommand]: http://click.palletsprojects.com/en/7.x/api/#click.Command
    """

    include_options_metavar = True

    def collect_usage_pieces(self, ctx: click.Context) -> List[str]:
        rv = [self.options_metavar] if self.include_options_metavar else []
        for param in self.get_params(ctx):
            if param.nargs == -1:
                rv.append("--")
            rv.extend(param.get_usage_pieces(ctx))
        return rv


class Group(Command, click.Group):
    """Base class for Queso command groups.

    A subclass of [Command](#command) and [click.Group][clickgroup].

    [clickgroup]: http://click.palletsprojects.com/en/7.x/api/#click.Group
    """


class FileGroup(Group):
    """A [Group](#group) that loads Queso commands declared in a file.

    # Parameters
    path (str):
        path to a Python module that contains Queso commands
        (declared with `@queso.command()` or `@queso.group()`).
    """

    def __init__(self, path: str, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)

        try:
            namespace = runpy.run_path(path)
        except FileNotFoundError:
            # User did not create custom commands
            return
        else:
            for value in namespace.values():
                if isinstance(value, Command):
                    self.add_command(value)


class CustomCommandsGroup(FileGroup):
    """A [FileGroup](#filegroup) that loads custom commands.

    The custom commands file is `./queso.py` by default. This can be
    overridden by setting the `QUESO_COMMANDS` environment variable.
    """

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(self.path(), *args, **kwargs)

    @staticmethod
    def path() -> str:
        return os.getenv("QUESO_COMMANDS", "queso.py")


C = TypeVar("C", bound=Command)
G = TypeVar("G", bound=Group)


def command(
    name: str = None, cls: C = None, **kwargs: Any
) -> Callable[[Callable], C]:
    """Replacement for `@click.command()`.
    
    Uses `Command` as a default base class.
    """
    if cls is None:
        cls = Command
    return click.command(name=name, cls=cls, **kwargs)


def group(
    name: str = None, cls: G = None, **kwargs: Any
) -> Callable[[Callable], G]:
    """Replacement for `click.group()`.

    Uses `Group` as a default base class.
    """
    if cls is None:
        cls = Group
    return click.group(name=name, cls=cls, **kwargs)
