from day18 import part1, part2, parse_math
from day18_part2 import parse_math as parse_math2


def test_parse_math_sample():
    assert parse_math('1 + 2 * 3 + 4 * 5 + 6') == 71


def test_parse_math_sample2():
    assert parse_math('1 + (2 * 3) + (4 * (5 + 6))') == 51


def test_parse_math_sample3():
    assert parse_math('2 * 3 + (4 * 5)') == 26


def test_parse_math_sample4():
    assert parse_math('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 437


def test_parse_math_sample5():
    assert parse_math('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 12240


def test_parse_math_sample6():
    assert parse_math('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 13632


def test_parse_math2_sample():
    assert parse_math2('1 + 2 * 3 + 4 * 5 + 6') == '231'


def test_parse_math2_sample2():
    assert parse_math2('1 + (2 * 3) + (4 * (5 + 6))') == '51'


def test_parse_math2_sample3():
    assert parse_math2('2 * 3 + (4 * 5)') == '46'


def test_parse_math2_sample4():
    assert parse_math2('5 + (8 * 3 + 9 + 3 * 4 * 3)') == '1445'


def test_parse_math2_sample5():
    assert parse_math2('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == '669060'


def test_parse_math2_sample6():
    assert parse_math2('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == '23340'
