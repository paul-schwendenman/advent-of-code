import pytest
import fileinput
from day14 import part1, part2, tilt, cycle_tilts


@pytest.fixture
def example_data():
    with fileinput.input('day14.example') as data:
        yield data


def test_part1_example(example_data):
    assert part1(example_data) == 136


def test_part2_example(example_data):
    assert part2(example_data) == 64


def test_tilt_north():
    grid = (((0, 0), '.'), ((0,1), 'O'), ((1, 0), '.'), ((1, 1), '.'))
    expt = (((0, 0), 'O'), ((0,1), '.'), ((1, 0), '.'), ((1, 1), '.'))

    assert tilt(grid, 2, 2, (0, -1)) == expt

def test_tilt_north_wall():
    grid = (((0, 0), '#'), ((0,1), 'O'), ((1, 0), '.'), ((1, 1), 'O'))
    expt = (((0, 0), '#'), ((0,1), 'O'), ((1, 0), 'O'), ((1, 1), '.'))

    assert tilt(grid, 2, 2, (0, -1)) == expt

def test_tilt_west():
    grid = (((0, 0), '.'), ((0,1), '.'), ((1, 0), 'O'), ((1, 1), '.'))
    expt = (((0, 0), 'O'), ((0,1), '.'), ((1, 0), '.'), ((1, 1), '.'))

    assert tilt(grid, 2, 2, (-1, 0)) == expt

def test_tilt_east():
    grid = (((0, 0), '.'), ((0,1), 'O'), ((1, 0), '.'), ((1, 1), '.'))
    expt = (((0, 0), '.'), ((0,1), '.'), ((1, 0), '.'), ((1, 1), 'O'))

    assert tilt(grid, 2, 2, (1, 0)) == expt

def test_tilt_south():
    grid = (((0, 0), 'O'), ((0,1), '.'), ((1, 0), '.'), ((1, 1), '.'))
    expt = (((0, 0), '.'), ((0,1), 'O'), ((1, 0), '.'), ((1, 1), '.'))

    assert tilt(grid, 2, 2, (0, 1)) == expt


def test_cycle():
    grid = (((0, 0), '#'), ((0,1), 'O'), ((1, 0), '.'), ((1, 1), 'O'))

    assert cycle_tilts(grid, 2, 2) == grid
