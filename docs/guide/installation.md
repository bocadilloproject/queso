# Installation

Boca is a Python package that was made to work hand in hand with [Bocadillo][bocadillo]. For most tasks, however, it can be used without having Bocadillo installed in your Python environment.

::: warning COMPATIBILITY NOTE
Boca is compatible with **Python 3.6+**.
:::

## From PyPI

Boca is released to PyPI, which means you can install using [pip](https://pip.pypa.io/en/stable/):

```bash
pip install boca
```

## From source (advanced)

For enthusiasts and contributors, Boca can also be installed from source.

You'll first need to clone the repository, then move to Bocadillo's root directory and run:

```bash
pip install .
```

Alternatively, use the `-e` option for an [editable installation](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs).

## Verifying your installation

To verify that Boca has been correctly installed and made available to your `PATH`, try obtaining its version in your shell:

```bash
$ boca -V
Boca: 0.1.1
Bocadillo: 0.10.1
Python: 3.7.2
OS: Darwin-18.2.0-x86_64-i386-64bit
```

Note that you may have another OS or a different version of Boca, Bocadillo, or Python installed.

[bocadillo]: https://bocadilloproject.github.io
