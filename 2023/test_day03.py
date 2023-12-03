import pytest
from day03 import part1, part2


@pytest.fixture
def example_data():
    yield [
        '467..114..\n',
        '...*......\n',
        '..35..633.\n',
        '......#...\n',
        '617*......\n',
        '.....+.58.\n',
        '..592.....\n',
        '......755.\n',
        '...$.*....\n',
        '.664.598..\n'
    ]


def test_part1_example(example_data):
    assert part1(example_data) == 4361


def test_part2_example(example_data):
    assert part2(example_data) == 467835
