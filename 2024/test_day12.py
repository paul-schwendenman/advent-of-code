import pytest
import fileinput
from day12 import part1, part2


@pytest.fixture
def example_data():
    with fileinput.input('day12.example') as data:
        yield data


@pytest.fixture
def example_data2():
    with fileinput.input('day12.example2') as data:
        yield data


@pytest.fixture
def example_data3():
    with fileinput.input('day12.example3') as data:
        yield data


def test_part1_example(example_data):
    assert part1(example_data) == 1930


def test_part1_example2(example_data2):
    assert part1(example_data2) == 140


def test_part1_example3(example_data3):
    assert part1(example_data3) == 772


def test_part2_example(example_data):
    assert part2(example_data) == 1206


def test_part2_example2(example_data2):
    assert part2(example_data2) == 80


def test_part2_example3(example_data3):
    assert part2(example_data3) == 436
