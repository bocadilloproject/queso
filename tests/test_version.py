import pytest
from bocadillo import __version__ as bocadillo_version

from queso import __version__ as package_version
from queso import create_cli
from queso.versions import get_versions

flags = ("-v", "-V", "--version", "version")


@pytest.mark.parametrize("flag", flags)
def test_all_flags_contain_bocadillo_and_boca_version(runner, flag):
    cli = create_cli()
    result = runner.invoke(cli, [flag])
    assert result.exit_code == 0
    assert bocadillo_version in result.output
    assert package_version in result.output


def test_invocations_have_the_same_output(runner):
    cli = create_cli()
    results = [runner.invoke(cli, [flag]) for flag in flags]
    assert all(result.exit_code == 0 for result in results)
    assert all(result.output == results[0].output for result in results)


@pytest.mark.parametrize("flag", flags)
def test_if_bocadillo_not_installed_then_placeholder_used(runner, flag):
    get_versions.simulate_module_not_found = True
    cli = create_cli()
    result = runner.invoke(cli, [flag])
    assert result.exit_code == 0
    assert "bocadillo: [not installed]" in result.output.lower()
