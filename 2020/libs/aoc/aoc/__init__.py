'''Advent Of Code Helpers

An implementation advent of code helper methods
'''
from contextlib import contextmanager
from typing import Any, List
import fileinput

__author__ = 'Paul Schwendenman'
__email__ = 'schwendenman.paul+aoc@gmail.com'
__license__ = 'MIT'
__version__ = '0.1.0'


@contextmanager
def readfile(filename=None):
    with fileinput.input(filename) as data:
        yield [line.rstrip() for line in data]


__all__: List[Any] = [readfile]
