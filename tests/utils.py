from contextlib import contextmanager
import os


@contextmanager
def env(var: str, value: str):
    initial = os.environ.get(var, None)
    os.environ[var] = value
    try:
        yield
    finally:
        os.environ.pop(var)
        if initial is not None:
            os.environ[var] = initial
