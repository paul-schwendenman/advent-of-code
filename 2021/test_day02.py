from contextlib import contextmanager
import fileinput
import pytest

from day02 import part1, part2


@contextmanager
def readfile(filename=None):
    with fileinput.input(filename) as data:
        yield [line.rstrip() for line in data]


@pytest.fixture
def input_data():
    with readfile("day02_input") as data:
        yield data


def test_part_1(input_data):
    assert part1(input_data) == 2272262


def test_part_2(input_data):
    assert part2(input_data) == 2134882034
