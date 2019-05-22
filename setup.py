import os

from setuptools import setup

setup(
  name="plz",
  version=os.environ.get("PLZ_VERSION", "1.0.9999"),
  packages=[ "plz", ],
  license="MIT",
  long_description=open("README.md").read(),
  entry_points={
    "console_scripts": ["plz=plz.main:main"],
  }
)
