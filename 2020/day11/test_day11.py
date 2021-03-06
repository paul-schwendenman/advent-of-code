from day11 import part1, part2


def test_part1_sample(sample_data):
    assert part1(sample_data) == 37


def test_part2_sample(sample_data):
    assert part2(sample_data) == 26


def test_part1_input(input_data):
    assert part1(input_data) == 2261


def test_part2_input(input_data):
    assert part2(input_data) == 2039
