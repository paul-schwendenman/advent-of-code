from day14 import part1, part2


def test_part1_sample(sample_data):
    assert part1(sample_data) == 165


def test_part2_sample(sample2_data):
    assert part2(sample2_data) == 208


def test_part1_input(input_data):
    assert part1(input_data) == 14553106347726


def test_part2_input(input_data):
    assert part2(input_data) == 2737766154126
