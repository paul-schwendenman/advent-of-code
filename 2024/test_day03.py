import pytest
import fileinput
from day03 import part1, part2


@pytest.fixture
def example_data():
    with fileinput.input('day03.example') as data:
        yield data


@pytest.fixture
def example2_data():
    with fileinput.input('day03.example2') as data:
        yield data


@pytest.fixture
def input_data():
    with fileinput.input('day3.in') as data:
        yield data


def test_part1_example(example_data):
    assert part1(example_data) == 161


def test_part2_example(example_data2):
    assert part2(example_data2) == 48


def test_part1_input(input_data):
    assert part1(input_data) == 174336360


def test_part2_input(input_data):
    assert part2(input_data) == 88802350
