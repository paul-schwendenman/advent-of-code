from day3 import (
    manhattan_distance,
    convert_instructions_to_path, main, main2,
    find_intersections, find_closest_intersection)


def test_manhattan():
    assert manhattan_distance((0, 0), (3, 3)) == 6


def test_manhattan2():
    assert manhattan_distance((0, 0), (155, 4)) == 159


def test_manhattan3():
    assert manhattan_distance((0, 0), (158, -12)) == 170


def test_line_up_coords():
    assert convert_instructions_to_path(["U2"]) == [(0, 1), (0, 2)]


def test_line_down_coords():
    assert convert_instructions_to_path(["D2"]) == [(0, -1), (0, -2)]


def test_line_right_coords():
    assert convert_instructions_to_path(["R3"]) == [(1, 0), (2, 0), (3, 0)]


def test_line_left_coords():
    assert convert_instructions_to_path(["L1"]) == [(-1, 0), ]


def test_complicated_coords():
    assert convert_instructions_to_path(["U3", "R3",  "D2", "L1"]) == [(0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (2, 1)]


def test_find_intersections():
    path1 = convert_instructions_to_path("R8,U5,L5,D3".split(','))
    path2 = convert_instructions_to_path("U7,R6,D4,L4".split(','))
    assert find_intersections(path1,  path2) == {(3, 3), (6, 5)}


def test_find_closest_intersection():
    assert find_closest_intersection({(3, 3), (6, 5)}) == 6


def test_main():
    assert main("R8,U5,L5,D3", "U7,R6,D4,L4") == 6


def test_main_2():
    assert main("R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83") == 159


def test_main_3():
    assert main("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7") == 135


def test_main2():
    assert main2("R8,U5,L5,D3", "U7,R6,D4,L4") == 30


def test_main2_2():
    assert main2("R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83") == 610


def test_main2_3():
    assert main2("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7") == 410
