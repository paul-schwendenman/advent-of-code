import pytest
from day10 import part1, part2, part2_dp, part2_math, readfile


@pytest.fixture
def sample_data():
    with readfile('sample') as data:
        yield data


@pytest.fixture
def input_data():
    with readfile('input') as data:
        yield data


def test_part1_sample(sample_data):
    assert part1(sample_data) == 35


def test_part2_sample(sample_data):
    assert part2(sample_data) == 8


def test_part2_dp_sample(sample_data):
    assert part2_dp(sample_data) == 8


def test_part2_math_sample(sample_data):
    assert part2_math(sample_data) == 8


def test_part1_input(input_data):
    assert part1(input_data) == 2343


def test_part2_input(input_data):
    assert part2(input_data) == 31581162962944


def test_part2_dp_input(input_data):
    assert part2_dp(input_data) == 31581162962944


def test_part2_math_input(input_data):
    assert part2_math(input_data) == 31581162962944
