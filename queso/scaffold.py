from os.path import abspath, dirname, join

SCAFFOLD_DIR = join(dirname(abspath(__file__)), "scaffolding")


def copy(filename: str, dest: str):
    path = join(SCAFFOLD_DIR, filename)
    with open(path, "r") as file_in, open(dest, "w") as file_out:
        file_out.write(file_in.read())
