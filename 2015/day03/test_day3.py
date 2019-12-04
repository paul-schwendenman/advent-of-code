from day3 import calculate_houses


def test_calculate_houses():
    assert calculate_houses('>') == 2


def test_calculate_houses2():
    assert calculate_houses('^>v<') == 4


def test_calculate_houses3():
    assert calculate_houses('^v^v^v^v^v') == 2
