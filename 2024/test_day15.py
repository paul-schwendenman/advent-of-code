import pytest
import fileinput
from day15 import part1, part2


@pytest.fixture
def example_data():
    with fileinput.input('day15.example') as data:
        yield data


@pytest.fixture
def example2_data():
    with fileinput.input('day15.example2') as data:
        yield data


def test_part1_example2(example2_data):
    assert part1(example2_data) == 2028


def test_part1_example(example_data):
    assert part1(example_data) == 10092


def test_part2_example(example_data):
    assert part2(example_data) == 9021
