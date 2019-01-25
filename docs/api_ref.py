import shutil
import subprocess
from glob import glob
from typing import List

import yaml

from boca.cli import create_cli


def get_help(cmd: List[str]):
    args = [*cmd, "--help"]
    result = subprocess.run(args, stdout=subprocess.PIPE)
    assert result.returncode == 0, result.returncode
    return "\n".join(["```", result.stdout.decode() + "```", ""])


def main():
    subprocess.call(["pydocmd", "generate"])

    cli = create_cli()

    with open("docs/reference/README.md", "w") as dest:

        def _header(level: int, label: str):
            dest.write(f"{level * '#'} {label}\n\n")

        def _text(content: str, nl=True):
            dest.write(content + (nl and "\n" or ""))

        _header(1, "Reference")

        _header(2, "Command line usage")

        _header(3, "Overview")
        _text(get_help(["boca"]))

        _header(3, "Built-in commands")
        for name in sorted(cli.commands.keys()):
            command = cli.commands[name]
            _header(4, name)
            _text("\n".join([command.__doc__ or "", get_help(["boca", name])]))

        _header(2, "Python modules")
        for path in glob("docs/reference/api/*.md"):
            with open(path) as source:
                for line in source:
                    if line.startswith("#"):
                        _header(2 + line.count("#"), line.lstrip("#"))
                    else:
                        _text(line, nl=False)

    with open("pydocmd.yml") as cfg:
        pydoc_config = yaml.safe_load(cfg)
    shutil.rmtree(pydoc_config["gens_dir"])


if __name__ == "__main__":
    main()
