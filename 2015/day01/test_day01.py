from day01 import count_parens


def test_count_parens():
    assert count_parens("()()") == 0


def test_count_parens2():
    assert count_parens("(())") == 0
