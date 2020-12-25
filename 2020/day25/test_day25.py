from day25 import handshake, brute_force_loop, part1


def test_handshake():
    assert handshake(7, 8) == 5764801


def test_handshake2():
    assert handshake(7, 11) == 17807724


def test_handshake3():
    assert handshake(17807724, 8) == 14897079


def test_handshake4():
    assert handshake(5764801, 11) == 14897079


def test_brute_force():
    assert brute_force_loop(7, 5764801) == 8


def test_brute_force2():
    assert brute_force_loop(7, 17807724) == 11


def test_part1_sample(sample_data):
    assert part1(sample_data) == 14897079
