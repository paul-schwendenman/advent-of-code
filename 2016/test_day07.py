import pytest
import fileinput
from day07 import part1, part2, check_ip


@pytest.fixture
def example_data():
    with fileinput.input('day07.example') as data:
        yield data


def test_check_ip_supports_tls():
    assert check_ip('abba[mnop]qrst')

def test_check_ip_square_bracket():
    assert not check_ip('abcd[bddb]xyyx')

def test_check_ip_matching_intieror_letters():
    assert not check_ip('aaaa[qwer]tyui')

def test_check_ip_supports_substring():
    assert check_ip('ioxxoj[asdfgh]zxcvbn')


def test_part1_example(example_data):
    assert part1(example_data) == 2


def test_part2_example(example_data):
    assert part2(example_data) == None
