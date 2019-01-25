"""Package setup."""

import setuptools

description = "Tasty development tooling for Bocadillo."

with open("README.md", "r") as readme:
    long_description = readme.read()

GITHUB = "https://github.com/bocadilloproject/boca"
DOCS = "https://bocadilloproject.github.io/boca"
CHANGELOG = f"{GITHUB}/blob/master/CHANGELOG.md"

setuptools.setup(
    name="boca",
    version="0.1.1",
    author="Florimond Manca",
    author_email="florimond.manca@gmail.com",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["boca"],
    install_requires=["click"],
    url=DOCS,
    project_urls={
        "Source": GITHUB,
        "Documentation": DOCS,
        "Changelog": CHANGELOG,
    },
    license="MIT",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
        "Topic :: Software Development :: Code Generators",
    ],
    entry_points={"console_scripts": ["boca=boca.__main__:cli"]},
)
