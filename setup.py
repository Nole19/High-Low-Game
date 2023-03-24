import codecs
import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

INSTALL_REQUIRES = [
    "requests",
    "bs4",
]

setup(
    name="high_low",
    version="1.0.0",
    description="The implementation of a high-low game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["high_low"],
    zip_safe=False,
    install_requires=INSTALL_REQUIRES,
)
