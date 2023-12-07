import pytest
import fileinput
from day07 import part1, part2


@pytest.fixture
def example_data():
    with fileinput.input('day07.example') as data:
        yield data


def test_part1_example(example_data):
    assert part1(example_data) == 6440


def test_part2_example(example_data):
    assert part2(example_data) == 5905
