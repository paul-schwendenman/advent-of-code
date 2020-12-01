from day10 import calc_angle, Point, calc_magnitude


# def test_main_1():
#     assert main('test1.in') == (Point(3, 4), 8)


# def test_main_2():
#     point, count = main('test2.in')
#     assert main('test2.in') == (Point(5, 8), 33)

def test_calc_angle_vertical():
    assert calc_angle(Point(5, 5), Point(5, 0)) == 0


def test_calc_angle_downward_vertical():
    assert calc_angle(Point(5, 5), Point(5, 10)) == 180


def test_calc_angle_horizontal():
    assert calc_angle(Point(5, 5), Point(10, 5)) == 90


def test_calc_angle_downward_horizontal():
    assert calc_angle(Point(5, 5), Point(0, 5)) == 270


def test_calc_magnitude_axis():
    assert calc_magnitude(Point(5, 5), Point(0, 5)) == 5


def test_calc_magnitude_60_degrees():
    assert calc_magnitude(Point(0, 0), Point(3, 4)) == 5
