from day02 import common, difference


def test_difference():
    assert difference('abcde', 'axcye') == 2


def test_difference2():
    assert difference('fghij', 'fguij') == 1


def test_common():
    assert common('fghij', 'fguij') == 'fgij'
