from day23 import part1, part2


def test_part1_sample_10_rounds():
    assert part1('389125467', 10) == '92658374'


def test_part1_sample_100_rounds():
    assert part1('389125467') == '67384529'


def test_part2_sample():
    assert part2('389125467') == 149245887792


def test_part1_input():
    assert part1('784235916') == '53248976'


def test_part2_input():
    assert part2('784235916') == 418819514477
