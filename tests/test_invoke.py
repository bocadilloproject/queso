from subprocess import call

import pytest


@pytest.mark.parametrize("command", [["boca"], ["python", "-m", "boca"]])
def test_invoke(command):
    assert call(command) == 0
