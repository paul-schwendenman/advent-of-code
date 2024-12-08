import pytest
import fileinput
from day08 import part1, part2


@pytest.fixture
def example_data():
    with fileinput.input('day08.example') as data:
        yield data
@pytest.fixture
def example_data2():
    with fileinput.input('day08_2.example') as data:
        yield data
@pytest.fixture
def example_data3():
    with fileinput.input('day08_3.example') as data:
        yield data


def test_part1_example(example_data):
    assert part1(example_data) == 14


def test_part1_example(example_data2):
    assert part1(example_data2) == 2


def test_part2_example(example_data):
    assert part2(example_data) == 34


def test_part2_example(example_data3):
    assert part2(example_data3) == 9
