from day12 import part1, part2


def test_part1_sample(sample_data):
    assert part1(sample_data) == 25


def test_part2_sample(sample_data):
    assert part2(sample_data) == 286


def test_part1_input(input_data):
    assert part1(input_data) == 1457


def test_part2_input(input_data):
    assert part2(input_data) == 106860
