import pytest
import fileinput
from day05 import part1, part2


@pytest.fixture
def example_data():
    with fileinput.input('day05.example') as data:
        yield data


def test_part1_example(example_data):
    assert part1(example_data) == '18f47a30'


def test_part2_example(example_data):
    assert part2(example_data) == '05ace8e3'
