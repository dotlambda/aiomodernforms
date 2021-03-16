#!/usr/bin/env python
"""The setup script."""
import os
import re
import sys

from setuptools import find_packages, setup


def get_version():
    """Get current version from code."""
    regex = r"__version__\s=\s\"(?P<version>[\d\.]+?)\""
    path = ("aiomodernforms", "__version__.py")
    return re.search(regex, read(*path)).group("version")


def read(*parts):
    """Read file."""
    filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts)
    sys.stdout.write(filename)
    with open(filename, encoding="utf-8", mode="rt") as fp:
        return fp.read()


with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="Brian Towles",
    author_email="brian@towles.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: AsyncIO",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    description="Asynchronous Python client for Modern Forms fans.",
    include_package_data=True,
    install_requires=["aiohttp>=3.0.0", "yarl", "backoff>=1.9.0", "packaging"],
    keywords=["modernforms", "api", "async", "client"],
    license="MIT license",
    long_description_content_type="text/markdown",
    long_description=readme,
    name="aiomodernforms",
    packages=find_packages(include=["aiomodernforms"]),
    test_suite="tests",
    url="https://github.com/wonderslug/aiomodernforms",
    version=get_version(),
    zip_safe=False,
)