import pytest
from aoc import readfile


@pytest.fixture
def sample_data():
    with readfile('sample') as data:
        yield data


@pytest.fixture
def input_data():
    with readfile('input') as data:
        yield data
