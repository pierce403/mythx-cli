#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

with open("requirements.txt", "r") as f:
    requirements = [x for x in map(str.strip, f.read().split("\n")) if x != ""]

setup_requirements = ["pytest-runner"]

test_requirements = ["pytest"]

setup(
    author="Dominik Muhs",
    author_email="dominik.muhs@consensys.net",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="A command line interface for the MythX smart contract security analysis API",
    entry_points={"console_scripts": ["mythx=mythx_cli.cli:cli"]},
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="mythx-cli",
    name="mythx_cli",
    packages=find_packages(exclude=["tests"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/dmuhs/mythx-cli",
    version="0.1.8",
    zip_safe=False,
)
