from day01 import part1, part2, prod

def test_day1_part1():
    assert part1([1721, 979, 366, 299, 675, 1456]) == 514579


def test_day1_part2():
    assert part2([1721, 979, 366, 299, 675, 1456]) == 241861950


def test_prod_two_numbers():
    assert prod(2, 3) == 6


def test_prod_three_numbers():
    assert prod(2, 3, 5) == 30
