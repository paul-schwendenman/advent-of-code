from day15 import part1


def test_day_15_0():
    assert part1("0,3,6", 10) == 0


def test_day_15_1():
    assert part1("0,3,6") == 436


def test_day_15_2():
    assert part1("1,3,2") == 0


def test_day_15_2():
    assert part1("2,1,3") == 10
