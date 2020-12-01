#!/usr/bin/env python
# Copyright 2019 Paul Schwendenman. All Rights Reserved.

from setuptools import setup
import intcode


setup(name='intcode',
      version=intcode.__version__,
      description=intcode.__doc__.strip(),
      long_description='',
      author=intcode.__author__,
      author_email=intcode.__email__,
      license=intcode.__license__,
      url='https://github.com/paul-schwendenman/advent-of-code-2019',
      packages=['intcode'],
      package_data={"intcode": ["py.typed"]},
      classifiers=[],
      )
