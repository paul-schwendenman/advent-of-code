from day24 import parse_instruction, Point


def test_parses_back_to_origin():
    assert parse_instruction("nwwswee") == Point(0, 0)


def test_parses_adjacent():
    assert parse_instruction("esew") == Point(1, -1)
