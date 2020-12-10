import pytest
from os.path import dirname, join
from day03 import part1, part2, readfile


@pytest.fixture
def sample_map():
    sample = join(dirname(__file__), 'sample')

    with readfile(sample) as data:
        yield data


def test_part1_sample(sample_map):
    assert part1(sample_map) == 7


def test_part2_sample(sample_map):
    assert part2(sample_map) == 336
