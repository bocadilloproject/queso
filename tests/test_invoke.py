from subprocess import call

import pytest


@pytest.mark.parametrize("command", [["queso"], ["python", "-m", "queso"]])
def test_invoke(command):
    assert call(command) == 0
