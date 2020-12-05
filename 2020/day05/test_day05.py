import pytest
from day05 import part1, part2, readfile


@pytest.fixture
def input_data():
    with readfile('input') as data:
        yield data


def test_part1_sample(input_data):
    assert part1(input_data) == 861


def test_part2_sample(input_data):
    assert part2(input_data) == 633
