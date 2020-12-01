from day16 import calc_pattern, find_digit


def test_find_digit():
    assert find_digit([1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 0, -1]) == 4


def test_calc_pattern():
    assert list(calc_pattern([0, 1, 0, -1], 1)) == [0, 1, 0, -1]


def test_calc_pattern2():
    assert list(calc_pattern([0, 1, 0, -1], 2)) == [0, 0, 1, 1, 0, 0, -1, -1]
