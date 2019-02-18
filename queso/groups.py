import click


class FileGroup(click.Group):
    """A Click [MultiCommand] that loads commands declared in a file.

    ::: warning
    You should not need to interact with this class directly.
    :::

    [MultiCommand]: http://click.palletsprojects.com/en/7.x/api/#click.MultiCommand

    # Parameters
    path (str):
        Path to a Python module declaring Click commands (declared with
        `@click.command()` or `@click.group()`).

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
