from day20 import part1, part2


def test_part1_sample(sample_data):
    assert part1(sample_data) == 20899048083289


def test_part2_sample(sample_data):
    assert part2(sample_data) == 273


def test_part1_input(input_data):
    assert part1(input_data) == 29293767579581


def test_part2_input(input_data):
    assert part2(input_data) == 1989
