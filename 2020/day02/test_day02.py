from day02 import part1, part2


def test_part1_sample_1():
    assert part1(['1-3 a: abcde']) == 1


def test_part1_sample_2():
    assert part1(['1-3 b: cdefg']) == 0


def test_part1_sample_3():
    assert part1(['2-9 c: ccccccccc']) == 1


def test_part1_sample():
    assert part1([
        '1-3 a: abcde\n',
        '1-3 b: cdefg\n',
        '2-9 c: ccccccccc\n'
    ]) == 2


def test_part2_sample_1():
    assert part2(['1-3 a: abcde']) == 1


def test_part2_sample_2():
    assert part2(['1-3 b: cdefg']) == 0


def test_part2_sample_3():
    assert part2(['2-9 c: ccccccccc']) == 0


def test_part2_sample():
    assert part2([
        '1-3 a: abcde\n',
        '1-3 b: cdefg\n',
        '2-9 c: ccccccccc\n'
    ]) == 1
