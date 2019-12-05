from day4 import calc_hash, check_hash, main


def test_calc_hash():
    assert calc_hash('abcdef', 609043) == '000001dbbfa3a5c83a2d506429c7b00e'


def test_check_hash():
    assert check_hash('000001dbbfa3a5c83a2d506429c7b00e')


def test_check_hash2():
    assert not check_hash('000011dbbfa3a5c83a2d506429c7b00e')


def test_main():
    assert main('abcdef') == 609043


def test_main():
    assert main('pqrstuv') == 1048970
