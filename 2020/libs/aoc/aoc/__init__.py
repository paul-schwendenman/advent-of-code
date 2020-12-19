'''Advent Of Code Helpers

An implementation advent of code helper methods
'''
from contextlib import contextmanager
from typing import Any, List
import fileinput
import time

__author__ = 'Paul Schwendenman'
__email__ = 'schwendenman.paul+aoc@gmail.com'
__license__ = 'MIT'
__version__ = '0.1.0'


@contextmanager
def readfile(filename=None):
    with fileinput.input(filename) as data:
        yield [line.rstrip() for line in data]


def profiler(func):
    def wrapper(*args, **kwargs):
        t = time.perf_counter_ns()
        result = func(*args, **kwargs)
        print(f'Timing {func.__name__}: {(time.perf_counter_ns()-t)/1000000:2.5f} ms')
        return result
    return wrapper


def tracer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        print(f'{func.__name__}({args}, {kwargs}) -> {result}')
        return result
    return wrapper


__all__: List[Any] = [readfile, profiler, tracer]
