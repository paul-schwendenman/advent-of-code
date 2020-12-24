from day24 import part1, part2, parse_instruction, Point


def test_parses_back_to_origin():
    assert parse_instruction("nwwswee") == Point(0, 0)


def test_parses_adjacent():
    assert parse_instruction("esew") == Point(1, -1)


def test_part1_sample(sample_data):
    assert part1(sample_data) == 10


def test_part2_sample(sample_data):
    assert part2(sample_data) == 2208


def test_part1_input(input_data):
    assert part1(input_data) == 386


def test_part2_input(input_data):
    assert part2(input_data) == 4214
