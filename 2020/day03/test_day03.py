import pytest
from day03 import part1, part2


@pytest.fixture
def sample_map():
    with open('sample') as input_file:
        yield input_file.read().splitlines()


def test_part1_sample(sample_map):
    assert part1(sample_map) == 7


def test_part2_sample(sample_map):
    assert part2(sample_map) == 336
