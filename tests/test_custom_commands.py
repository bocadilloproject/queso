from inspect import cleandoc

import pytest

from boca import create_cli
from boca.custom import CUSTOM_COMMANDS_ENV_VAR

from .utils import env


def test_can_init_custom_commands(runner, tmpdir):
    cli = create_cli()

    result = runner.invoke(cli, ["init:custom", "-d", str(tmpdir)])
    output = result.output.lower()

    assert result.exit_code == 0, output

    for item in "generated", "open the file":
        assert item in output


def test_can_provide_custom_commands(runner, tmpdir):
    boca_dot_py = tmpdir.join("boca.py")

    boca_dot_py.write(
        cleandoc(
            """
    import click

    @click.group()
    def cli():
        pass

    @cli.command()
    def hello():
        click.echo("Hello!")
    """
        )
    )

    with env(CUSTOM_COMMANDS_ENV_VAR, str(boca_dot_py)):
        cli = create_cli()

    result = runner.invoke(cli, ["hello"])

    assert result.exit_code == 0
    assert result.output == "Hello!\n"


def test_at_least_one_group_is_expected(tmpdir):
    boca_dot_py = tmpdir.join("boca.py")
    boca_dot_py.write("import click")

    with env(CUSTOM_COMMANDS_ENV_VAR, str(boca_dot_py)):
        with pytest.raises(ValueError):
            create_cli()
