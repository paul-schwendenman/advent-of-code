from day05 import line_to_array

def test_vertical_line():
    assert list(line_to_array('1,1 -> 1,3')) == [(1, 1), (1, 2), (1, 3)]

def test_horizontal_line():
    assert list(line_to_array('9,7 -> 7,7')) == [(9, 7), (8, 7), (7, 7)]

def test_ignores_diagonal_line():
    assert list(line_to_array('1,1 -> 3,3')) == []

def test_diagonal_line():
    assert list(line_to_array('1,1 -> 3,3', include_diagonals=True)) == [(1, 1), (2, 2), (3, 3)]

def test_other_diagonal_line():
    assert list(line_to_array('9,7 -> 7,9', include_diagonals=True)) == [(9, 7), (8, 8), (7, 9)]
