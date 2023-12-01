from day01 import walk_path


def test_example_1():
    assert walk_path(['R2', 'L3']) == 5

def test_example_2():
    assert walk_path(['R2', 'R2', 'R2']) == 2

def test_example_3():
    assert walk_path(['R5', 'L5', 'R5', 'R3']) == 12
