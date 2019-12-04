from day01 import count_parens, find_basement


def test_count_parens():
    assert count_parens("()()") == 0


def test_count_parens2():
    assert count_parens("(())") == 0


def test_count_parens3():
    assert count_parens("(((") == 3


def test_count_parens4():
    assert count_parens("(()(()(") == 3


def test_count_parens5():
    assert count_parens("))(((((") == 3


def test_count_parens6():
    assert count_parens("())") == -1


def test_count_parens7():
    assert count_parens("))(") == -1


def test_count_parens8():
    assert count_parens(")))") == -3


def test_count_parens9():
    assert count_parens(")())())") == -3


def test_find_basement():
    assert find_basement(")") == 1


def test_find_basement2():
    assert find_basement("()())") == 5
