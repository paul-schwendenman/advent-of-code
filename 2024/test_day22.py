import pytest
import fileinput
from day22 import part1, part2


@pytest.fixture
def example_data():
    with fileinput.input('day22.example') as data:
        yield data


@pytest.fixture
def example2_data():
    with fileinput.input('day22.example2') as data:
        yield data


@pytest.fixture
def example3_data():
    with fileinput.input('day22.example3') as data:
        yield data


def test_part1_example(example2_data):
    assert part1(example2_data) == 37327623


def test_part2_example(example3_data):
    assert part2(example3_data) == 23
