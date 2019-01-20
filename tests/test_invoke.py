from subprocess import call


def test_invoke():
    assert call(["boca"]) == 0
