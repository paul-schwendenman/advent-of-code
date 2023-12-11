import pytest
import fileinput
from day11 import part1, part2


@pytest.fixture
def example_data():
    with fileinput.input('day11.example') as data:
        yield data


def test_part1_example(example_data):
    assert part1(example_data) == 374


def test_part2_example(example_data):
    assert part2(example_data, 10) == 1030


def test_part2_exampl_100(example_data):
    assert part2(example_data, 100) == 8410
