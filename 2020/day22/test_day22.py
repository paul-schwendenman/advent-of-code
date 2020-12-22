from day22 import part1, part2


def test_part1_sample(sample_data):
    assert part1(sample_data) == 306


def test_part2_sample(sample_data):
    assert part2(sample_data) == 291


def test_part1_input(input_data):
    assert part1(input_data) == 33694


def test_part2_input(input_data):
    assert part2(input_data) == 0
