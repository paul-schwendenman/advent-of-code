import pytest
import fileinput
from day09 import part1, part2, decompress, decompress2


@pytest.fixture
def example_data():
    with fileinput.input('day09.example') as data:
        yield data


def test_decompress_advent():
    # assert len(decompress('ADVENT')) == 6
    assert (decompress('ADVENT')) == 'ADVENT'


def test_decompress_repeats_value():
    assert (decompress('A(1x5)BC')) == 'ABBBBBC'
    # assert len(decompress('A(1x5)BC')) == 7


def test_decompress_triple():
    assert (decompress('(3x3)XYZ')) == 'XYZXYZXYZ'
    assert len(decompress('(3x3)XYZ')) == 9


def test_decompress_two_times():
    assert len(decompress('A(2x2)BCD(2x2)EFG')) == 11


def test_decompress_data():
    assert len(decompress('(6x1)(1x3)A')) == 6


def test_decompress_double():
    assert len(decompress('X(8x2)(3x3)ABCY')) == 18


def test_part1_example(example_data):
    assert part1(example_data) == 18


def test_decompress_triple():
    assert (decompress2('(3x3)XYZ')) == 'XYZXYZXYZ'
    assert len(decompress2('(3x3)XYZ')) == 9


def test_decompress_double():
    assert (decompress2('X(8x2)(3x3)ABCY')) == 'XABCABCABCABCABCABCY'


def test_decompress_a_s():
    assert len(decompress2('(27x12)(20x12)(13x14)(7x10)(1x12)A')) == 241920


def test_decompress_long():
    assert len(decompress2('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN')) == 445


def test_part2_example(example_data):
    assert part2(example_data) == None
