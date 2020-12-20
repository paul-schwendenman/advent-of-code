from day19 import part1, part2


def test_part1_sample(sample_data):
    assert part1(sample_data) == 2


def test_part1_sample2(sample2_data):
    assert part1(sample2_data) == 3


def test_part1_input(input_data):
    assert part1(input_data) == 118


def test_part2_sample2(sample2_data):
    assert part2(sample2_data) == 12


def test_part2_input(input_data):
    assert part2(input_data) == 246
