# boca.py
import click


@click.command()
def fail():
    raise RuntimeError("This is unexpected…")
