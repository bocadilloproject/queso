from pathlib import Path

TEMPLATES_DIR = Path(__file__).parent / "templates"


def copy(filename: str, dest: str):
    source = str(TEMPLATES_DIR / filename)
    with open(source, "r") as source_file, open(dest, "w") as dest_file:
        dest_file.write(source_file.read())
