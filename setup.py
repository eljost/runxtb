#!/usr/bin/env python3

from setuptools import find_packages, setup
import sys

if sys.version_info.major < 3:
    raise SystemExit("Python 3 is required!")

setup(
    name="runxtb",
    version="0.0.1",
    description="Simple GUI for calling xtb",
    url="https://github.com/eljost/runxtb",
    maintainer="Johannes Steinmetzer",
    maintainer_email="johannes.steinmetzer@uni-jena.de",
    license="GPL 3",
    platforms=["unix"],
    packages=find_packages(),
    #install_requires=[
    #    "pyqt",
    #],
    entry_points={
        "console_scripts": [
            "runxtb = runxtb.run:main",
        ]
    },
)
