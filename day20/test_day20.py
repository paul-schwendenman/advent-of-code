from day20 import Point, get_portal_neighboor, get_portal_name, get_portal_location


def test_Point_get_neighboors():
    expected_points = [Point(x=-1, y=0), Point(x=1, y=0), Point(x=0, y=-1), Point(x=0, y=1)]
    assert list(Point(0, 0).get_neighboors()) == expected_points


def test_Point_addition():
    assert Point(1, 2) + Point(1, 2) == Point(2, 4)


def test_get_portal_neighboor():
    grid = [
        '  A   ',
        '  A   ',
        '##.###',
    ]
    assert get_portal_neighboor(Point(2, 0), grid) == Point(2, 1)


def test_get_portal_neighboor2():
    grid = [
        '  A   ',
        '  A   ',
        '##.###',
    ]
    assert get_portal_neighboor(Point(2, 1), grid) == Point(2, 0)


def test_get_portal_neighboor3():
    grid = [
        '   #  ',
        ' AA.  ',
        '   #  ',
    ]
    assert get_portal_neighboor(Point(2, 1), grid) == Point(1, 1)


def test_get_portal_name():
    grid = [
        '   #  ',
        ' AA.  ',
        '   #  ',
    ]
    assert get_portal_name(Point(2, 1), grid) == 'AA'


def test_get_portal_location():
    grid = [
        '   #  ',
        ' AA.  ',
        '   #  ',
    ]
    assert get_portal_location(Point(2, 1), grid) == Point(3, 1)
