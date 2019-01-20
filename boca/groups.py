import click


class FileGroup(click.Group):
    """A Click [MultiCommand] that loads a group of commands from a file.

    ::: warning
    You should not need to interact with this class directly.
    :::

    [MultiCommand]: http://click.palletsprojects.com/en/7.x/api/#click.MultiCommand

    # Parameters
    path (str):
        Path to a Python module declaring at least one Click group, from which
        extra commands will be obtained.

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

        groups = (
            val for val in namespace.values() if isinstance(val, click.Group)
        )
        group = next(groups, None)
        if group is None:
            raise ValueError(
                f"Expected at least one group in {path}, none found."
            )
        for name, cmd in group.commands.items():
            self.add_command(cmd, name)
