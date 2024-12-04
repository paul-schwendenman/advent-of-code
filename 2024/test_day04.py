import pytest
import fileinput
from day04 import part1, part2, Offset


@pytest.fixture
def example_data():
    with fileinput.input('day04.example') as data:
        yield data


def test_part1_example(example_data):
    assert part1(example_data) == 18


def test_part2_example(example_data):
    assert part2(example_data) == 9


def test_left_opposite_of_right():
    assert Offset.LEFT * -1 == Offset.RIGHT

def test_right_opposite_of_left():
    assert Offset.RIGHT * -1 == Offset.LEFT

def test_up_opposite_of_down():
    assert Offset.UP * -1 == Offset.DOWN

def test_down_opposite_of_up():
    assert Offset.DOWN * -1 == Offset.UP

def test_top_left_opposite_of_bottom_right():
    assert Offset.TOP_LEFT * -1 == Offset.BOTTOM_RIGHT

def test_bottom_right_opposite_of_top_left():
    assert Offset.BOTTOM_RIGHT * -1 == Offset.TOP_LEFT

def test_top_right_opposite_of_bottom_left():
    assert Offset.TOP_RIGHT * -1 == Offset.BOTTOM_LEFT

def test_bottom_left_opposite_of_top_right():
    assert Offset.BOTTOM_LEFT * -1 == Offset.TOP_RIGHT

def test_can_scale_offset():
    assert Offset.BOTTOM_RIGHT * 3 == (3, 3)
