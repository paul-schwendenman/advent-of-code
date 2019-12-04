from day02 import (
    get_dimensions, calculate_surface_area, calculate_paper_needed)


def test_get_dimensions():
    assert get_dimensions("2x4x5") == [2, 4, 5]


def test_get_dimensions2():
    assert get_dimensions("5x4x3") == [3, 4, 5]


def test_calculate_surface_area():
    assert calculate_surface_area(2, 3, 4) == 52


def test_calculate_surface_area2():
    assert calculate_surface_area(1, 1, 10) == 42


def test_calculate_paper_needed():
    assert calculate_paper_needed(2, 3, 4) == 58


def test_calculate_paper_needed2():
    assert calculate_paper_needed(1, 1, 10) == 43
