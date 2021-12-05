from contextlib import contextmanager
import fileinput
import pytest

from day03 import part1, part2


@contextmanager
def readfile(filename=None):
    with fileinput.input(filename) as data:
        yield [line.rstrip() for line in data]


@pytest.fixture
def input_data():
    with readfile("day03_input") as data:
        yield data

@pytest.fixture
def sample_data():
    with readfile("day03_sample") as data:
        yield data


def test_part_1_sample(sample_data):
    assert part1(sample_data) == 198


def test_part_1(input_data):
    assert part1(input_data) == 2595824


def test_part_2_sample(sample_data):
    assert part2(sample_data) == 230


def test_part_2(input_data):
    assert part2(input_data) == 2135254
