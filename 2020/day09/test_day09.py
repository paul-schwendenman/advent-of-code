import pytest
from day09 import find_invalid_number, find_contiguous_set, part1, part2, readfile


@pytest.fixture
def sample_data():
    with readfile('sample') as data:
        yield data


@pytest.fixture
def input_data():
    with readfile('input') as data:
        yield data


def test_part1_sample(sample_data):
    numbers = [int(num) for num in sample_data]

    assert find_invalid_number(numbers, 5) == 127


def test_part2_sample(sample_data):
    numbers = [int(num) for num in sample_data]
    goal = 127

    assert find_contiguous_set(numbers, goal) == (2, 6)


def test_part1_input(input_data):
    assert part1(input_data) == 556543474


def test_part2_input(input_data):
    goal = 556543474
    assert part2(input_data, goal) == 76096372
