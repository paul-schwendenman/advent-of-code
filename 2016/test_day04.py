import pytest
import fileinput
from day04 import part1, part2, check_room, calc_checksum


@pytest.fixture
def example_data():
    with fileinput.input('day04.example') as data:
        yield data


def test_checksum_example1():
    assert calc_checksum('aaaaa-bbb-z-y-x') == 'abxyz'


def test_checksum_example2():
    assert calc_checksum('a-b-c-d-e-f-g-h') == 'abcde'


def test_checksum_example3():
    assert calc_checksum('not-a-real-room') == 'oarel'


def test_room_example1():
    assert check_room('aaaaa-bbb-z-y-x-123[abxyz]').valid


def test_room_example2():
    assert check_room('a-b-c-d-e-f-g-h-987[abcde]').valid


def test_room_example3():
    assert check_room('not-a-real-room-404[oarel]').valid


def test_room_example4():
    assert not check_room('totally-real-room-200[decoy]').valid


def test_room_decryption():
    assert check_room('qzmt-zixmtkozy-ivhz-343').name == 'very encrypted name'


def test_part1_example(example_data):
    assert part1(example_data) == 1514


def test_part2_example(example_data):
    assert part2(example_data) == None
