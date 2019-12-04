from day4 import has_double_digit, has_double_digit2, never_decreases


def test_has_double_digit():
    assert has_double_digit(122345)


def test_does_not_have_double_digit():
    assert not has_double_digit(123456)


def test_has_double_digit2():
    assert has_double_digit2(112233)


def test_has_double_digit2_2():
    assert has_double_digit2(111144)


def test_does_not_have_double_digit2():
    assert not has_double_digit2(123444)


def test_never_decreases():
    assert never_decreases("123455")


def test_not_decreasing():
    assert not never_decreases("123450")
