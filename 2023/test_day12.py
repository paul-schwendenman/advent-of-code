import pytest
import fileinput
from day12 import part1, part2, score_springs


@pytest.fixture
def example_data():
    with fileinput.input('day12.example') as data:
        yield data


@pytest.mark.skip()
def test_part1_example(example_data):
    assert part1(example_data) == 21


def test_part2_example(example_data):
    assert part2(example_data) == None


def test_score_springs_1():
    '''
    #.#.### 1,1,3
    '''
    assert score_springs("#.#.###") == [1, 1, 3]

def test_score_springs_2():
    '''
    .#...#....###. 1,1,3
    '''
    assert score_springs(".#...#....###.") == [1, 1, 3]

def test_score_springs_3():
    '''
    .#.###.#.###### 1,3,1,6
    '''
    assert score_springs(".#.###.#.######") == [1, 3, 1, 6]

def test_score_springs_4():
    '''
    ####.#...#... 4,1,1
    '''
    assert score_springs("####.#...#...") == [4, 1, 1]

def test_score_springs_5():
    '''
    #....######..#####. 1,6,5
    '''
    assert score_springs("#....######..#####.") == [1, 6, 5]

def test_score_springs_6():
    '''
    .###.##....# 3,2,1
    '''
    assert score_springs(".###.##....#") == [3, 2, 1]
