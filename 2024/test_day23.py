import pytest
import fileinput
from day23 import part1, part2


@pytest.fixture
def example_data():
    with fileinput.input('day23.example') as data:
        yield data


def test_part1_example(example_data):
    assert part1(example_data) == 7


def test_part2_example(example_data):
    assert part2(example_data) == 'co,de,ka,ta'


def test_part1_speed(benchmark, example_data):
    lines = [line for line in example_data]
    value = benchmark(part1, lines)

    assert value == 7


def test_part2_speed(benchmark, example_data):
    lines = [line for line in example_data]
    value = benchmark(part2, lines)

    assert value == 'co,de,ka,ta'
