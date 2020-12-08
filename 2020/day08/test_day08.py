import pytest
from day08 import part1, part2, readfile


@pytest.fixture
def sample_data():
    with readfile('sample') as data:
        yield data


def test_part1_sample(sample_data):
    assert part1(sample_data) == 5


def test_part2_sample(sample_data):
    assert part2(sample_data) == 8
