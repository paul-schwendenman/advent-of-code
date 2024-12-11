import pytest
import fileinput
from day11 import part1, part2, solve


@pytest.fixture
def example_data():
    with fileinput.input('day11.example') as data:
        yield data


@pytest.fixture
def input_data():
    with fileinput.input('day11.in') as data:
        yield data


def test_part1_example(example_data):
    assert part1(example_data) == 55312


def test_part1_input(input_data):
    assert part1(input_data) == 191690


def test_part2_example(input_data):
    assert part2(input_data) == 228651922369703


def test_solve_benchmark(benchmark):
    input = "30 71441 3784 580926 2 8122942 0 291"
    value = benchmark(solve, input)
    assert value == 228651922369703
