"""
# click-creds
Pluggable credentials storage and management for click CLI apps.
## Docs & Example Usage: https://github.com/eshaan7/click-creds
"""

import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

VERSION = (HERE / "version.txt").read_text()

GITHUB_URL = "https://github.com/eshaan7/click-creds"

requirements = (HERE / "requirements.txt").read_text().split("\n")

requirements_test = (HERE / "requirements.dev.txt").read_text().split("\n")

# This call to setup() does all the work
setup(
    name="click-creds",
    version=VERSION,
    url=GITHUB_URL,
    license="BSD",
    author="Eshaan Bansal",
    author_email="eshaan7bansal@gmail.com",
    description="Pluggable credentials storage and management for click CLI apps.",
    long_description=README,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    py_modules=["click_creds"],
    packages=["click_creds"],
    zip_safe=False,
    include_package_data=True,
    install_requires=requirements,
    keywords="click credentials creds netrc auth cli python store",
    project_urls={
        "Documentation": GITHUB_URL,
        "Funding": "https://www.paypal.me/eshaanbansal",
        "Source": GITHUB_URL,
        "Tracker": "{}/issues".format(GITHUB_URL),
    },
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 5 - Production/Stable",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Environment :: Web Environment",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        "dev": requirements_test + requirements,
        "test": requirements_test + requirements,
    },
)
