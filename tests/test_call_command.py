import pytest
import click
from click.exceptions import UsageError

from boca import call_command


def test_simple_call():
    r = call_command("version")
    assert r.exit_code == r.value == 0
    assert "Boca: " in r.output


def test_call_with_parameters():
    r = call_command("version", "--help")
    assert r.exit_code == r.value == 0
    assert "Usage: boca version" in r.output


def test_click_exceptions_are_propagated():
    with pytest.raises(UsageError):
        call_command("noisrev")


def test_capture_click_exception():
    r = call_command("noisrev", capture_errors=True)
    assert r.exit_code == 2
    assert r.value is None
    assert "No such command" in r.output


def test_capture_non_click_exception():
    @click.group()
    def cli():
        pass

    @cli.command()
    def fail():
        raise RuntimeError("Oops")

    with pytest.raises(RuntimeError):
        call_command("fail", cli=cli, capture_errors=True)

    r = call_command("fail", cli=cli, capture_errors=all)
    assert r.exit_code == 2
    assert r.value is None
    assert "Traceback" in r.output
    assert "Oops" in r.output

