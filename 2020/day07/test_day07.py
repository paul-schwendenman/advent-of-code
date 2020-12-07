import pytest
from day07 import part1, part2, readfile


@pytest.fixture
def sample_data():
    with readfile('sample') as data:
        yield data


@pytest.fixture
def sample2_data():
    with readfile('sample2') as data:
        yield data


def test_part1_sample(sample_data):
    assert part1(sample_data) == 4


def test_part2_sample(sample_data):
    assert part2(sample_data) == 32


def test_part2_sample2(sample2_data):
    assert part2(sample2_data) == 126
