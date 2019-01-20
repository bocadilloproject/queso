import pytest

from boca import __version__, create_cli


@pytest.mark.parametrize("flag", ["-v", "-V", "--version", "version"])
def test_get_version(runner, flag):
    cli = create_cli()

    result = runner.invoke(cli, [flag])
    assert result.exit_code == 0
    assert __version__ in result.output
