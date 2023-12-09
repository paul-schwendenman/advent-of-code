import pytest
import fileinput
from day09 import part1, part2, extend_sequence


@pytest.fixture
def example_data():
    with fileinput.input('day09.example') as data:
        yield data


def test_part1_example(example_data):
    assert part1(example_data) == 114


def test_part2_example(example_data):
    assert part2(example_data) == 2


def test_solve_handles_base_case():
    assert extend_sequence([0, 0, 0, 0]) == [0, 0]


def test_solve_handles_constant_velocity():
    assert extend_sequence([2, 2, 2]) == [2, 2]


def test_solve_handles_increasing_velocity():
    assert extend_sequence([2, 4, 6]) == [0, 8]

def test_solve_handles_increasing_acceleration():
    assert extend_sequence([10, 13, 16, 21, 30, 45]) == [5, 68]
