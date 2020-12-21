from day21 import part1, part2


def test_part1_sample(sample_data):
    assert part1(sample_data) == 5


def test_part2_sample(sample_data):
    assert part2(sample_data) == 'mxmxvkd,sqjhc,fvjkl'


def test_part1_input(input_data):
    assert part1(input_data) == 2282


def test_part2_input(input_data):
    assert part2(input_data) == 'vrzkz,zjsh,hphcb,mbdksj,vzzxl,ctmzsr,rkzqs,zmhnj'
