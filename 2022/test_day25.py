from day25 import from_snafu, to_snafu
import pytest

test_data = [
    ('1', 1),
    ('2', 2),
    ('1=', 3),
    ('1-', 4),
    ('10', 5),
    ('11', 6),
    ('12', 7),
    ('2=', 8),
    ('2-', 9),
    ('20', 10),
    ('1=0', 15),
    ('1-0', 20),
    ('1=11-2', 2022),
    ('1-0---0', 12345),
    ('1121-1110-1=0', 314159265),
]


test_data2 = [
    ('1=-0-2', 1747),
    ('12111', 906),
    ('2=0=', 198),
    ('21', 11),
    ('2=01', 201),
    ('111', 31),
    ('20012', 1257),
    ('112', 32),
    ('1=-1=', 353),
    ('1-12', 107),
    ('12', 7),
    ('1=', 3),
    ('122', 37),
]


@pytest.mark.parametrize('snafu,expected', test_data)
def test_number_from_snafu(snafu, expected):
    assert from_snafu(snafu) == expected


@pytest.mark.parametrize('expected,number', test_data)
def test_number_to_snafu(number, expected):
    assert to_snafu(number) == expected


@pytest.mark.parametrize('snafu,expected', test_data2)
def test_number_from_snafu2(snafu, expected):
    assert from_snafu(snafu) == expected


@pytest.mark.parametrize('expected,number', test_data2)
def test_number_to_snafu2(number, expected):
    assert to_snafu(number) == expected
