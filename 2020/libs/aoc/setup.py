#!/usr/bin/env python
# Copyright 2019 Paul Schwendenman. All Rights Reserved.

from setuptools import setup, find_packages
import aoc


setup(name='aoc',
      version=aoc.__version__,
      description=aoc.__doc__.strip(),
      long_description='',
      author=aoc.__author__,
      author_email=aoc.__email__,
      license=aoc.__license__,
      url='https://github.com/paul-schwendenman/advent-of-code/libs/aoc/',
      packages=find_packages(),
      package_data={"aoc": ["py.typed"]},
      classifiers=[],
      )
