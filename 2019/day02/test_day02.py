from day02 import parse_program, run_program, combine

def test_parse_program():
    assert list(parse_program("1,9,10,70")) == [1, 9, 10, 70]

def test_empty_program():
    assert run_program([99]) == [99]

def test_simple_addition_program():
    assert run_program([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]

def test_simple_multiplication_program():
    assert run_program([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]

def test_out_of_bounds_memory():
    assert run_program([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]

def test_multiple_operations():
    assert run_program([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]

def test_combine_noun_and_verb():
    assert combine(noun=12, verb=2) == 1202
