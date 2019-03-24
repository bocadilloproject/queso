from inspect import cleandoc
from os.path import join

import pytest

from queso import create_cli, call_command

from .utils import override_env


def test_init_custom_commands_in_dir(runner, tmpdir):
    cli = create_cli()

    result = runner.invoke(cli, ["init:custom", "-d", str(tmpdir)])
    output = result.output.lower()

    assert result.exit_code == 0, output

    for item in "generated", "open the file":
        assert item in output

    with open(join(str(tmpdir), "queso.py"), "r") as generated:
        assert "import click" in generated.read()


@pytest.fixture(name="custom_commands")
def fixture_custom_commands(tmpdir):
    file_ = tmpdir.join("queso.py")
    file_.write(
        cleandoc(
            """
    import click

    @click.group()
    def animals():
        pass

    @animals.command()
    def cats():
        click.echo("Cats!")

    @click.command(name="the-cars")
    def cars():
        click.echo("Cars!")
    """
        )
    )
    return str(file_)


@pytest.mark.parametrize(
    "command, exit_code, sample",
    [
        (["animals"], 0, "Usage: queso animals"),
        (["cats"], 0, "Cats!"),
        (["the-cars"], 0, "Cars!"),
        (["cars"], 2, "Usage: queso"),
    ],
)
def test_can_provide_custom_commands(
    runner, custom_commands, command, exit_code, sample
):
    with override_env("QUESO_COMMANDS", custom_commands):
        cli = create_cli()

    result = runner.invoke(cli, command)
    assert result.exit_code == exit_code
    assert sample in result.output


def test_no_commands_allowed(tmpdir):
    boca_dot_py = tmpdir.join("queso.py")
    boca_dot_py.write("import click")
    create_cli()


def test_call_custom_command(custom_commands):
    with override_env("QUESO_COMMANDS", custom_commands):
        r = call_command("cats")
        assert r.exit_code == 0
        assert r.value is None
        assert "Cats!" in r.output
