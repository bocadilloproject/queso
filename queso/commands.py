import os

import click


class QuesoCommand(click.Command):
    """Base class for Queso commands."""

    include_options_metavar = True

    def collect_usage_pieces(self, ctx):
        rv = [self.options_metavar] if self.include_options_metavar else []
        for param in self.get_params(ctx):
            if param.nargs == -1:
                rv.append("--")
            rv.extend(param.get_usage_pieces(ctx))
        return rv


class FileGroup(click.Group):
    """A Click [MultiCommand] that loads commands declared in a file.

    [MultiCommand]: http://click.palletsprojects.com/en/7.x/api/#click.MultiCommand

    # Parameters
    path (str):
        path to a Python module that contains Click commands
        (declared with `@click.command()` or `@click.group()`).
    """

    def __init__(self, path: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._load_group(path)

    def _load_group(self, path: str):
        namespace = {}

        try:
            with open(path, "r") as f:
                code = compile(source=f.read(), filename=path, mode="exec")
        except FileNotFoundError:
            # User did not create custom commands
            return
        else:
            eval(code, namespace, namespace)

        for value in namespace.values():
            if isinstance(value, click.Command):
                self.add_command(value)


class CustomCommandsGroup(FileGroup):
    """A [FileGroup](#filegroup) which looks for custom commands.

    The custom commands file is `./queso.py` by default. This can be
    overridden by setting the `QUESO_COMMANDS` environment variable.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(self.path(), *args, **kwargs)

    @staticmethod
    def path():
        return os.getenv("QUESO_COMMANDS", "queso.py")
