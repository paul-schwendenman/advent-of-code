import pytest
from day05 import find_seat_id, part1, part2, readfile


@pytest.fixture
def input_data():
    with readfile('input') as data:
        yield data


def test_find_seat_id_357():
    assert find_seat_id('FBFBBFFRLR') == 357


def test_find_seat_id_567():
    assert find_seat_id('BFFFBBFRRR') == 567


def test_find_seat_id_119():
    assert find_seat_id('FFFBBBFRRR') == 119


def test_find_seat_id_820():
    assert find_seat_id('BBFFBBFRLL') == 820


def test_part1_sample(input_data):
    assert part1(input_data) == 861


def test_part2_sample(input_data):
    assert part2(input_data) == 633
