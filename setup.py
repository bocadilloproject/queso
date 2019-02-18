"""Package setup."""

import setuptools

description = "Tasty development tooling for Bocadillo."

with open("README.md", "r") as readme:
    long_description = readme.read()

GITHUB = "https://github.com/bocadilloproject/queso"
DOCS = "https://bocadilloproject.github.io/queso"
CHANGELOG = f"{GITHUB}/blob/master/CHANGELOG.md"

setuptools.setup(
    name="queso",
    version="0.2.0",
    author="Florimond Manca",
    author_email="florimond.manca@gmail.com",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["queso"],
    install_requires=["click"],
    url=DOCS,
    project_urls={
        "Source": GITHUB,
        "Documentation": DOCS,
        "Changelog": CHANGELOG,
    },
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
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
    entry_points={"console_scripts": ["queso=queso.__main__:cli"]},
)
