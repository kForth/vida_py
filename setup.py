#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as readme_file:
    readme = readme_file.read()

with open("requirements.txt", encoding="utf-8") as req_file:
    requirements = req_file.readlines()

setup(
    author="Kestin Goforth",
    author_email="kgoforth1503@gmail.com",
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    description="Python interface for Volvo's VIDA databases.",
    entry_points={
        "console_scripts": [
            "py_vida=py_vida:main",
        ],
    },
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords="VIDA, volvo",
    name="py_vida",
    packages=find_packages(include=["py_vida", "py_vida.*"]),
    url="https://github.com/kForth/py_vida.git",
    version="0.1.0",
    zip_safe=False,
)
