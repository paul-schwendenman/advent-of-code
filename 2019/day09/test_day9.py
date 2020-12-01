from day9 import main, run_program


def test_main():
    assert main(1, 'day09/input') == [3507134798]


def test_main2():
    assert main(2, 'day09/input') == [84513]


def test_returns_self():
    program = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
    expected_output = [int(a) for a in program.split(',')]
    assert run_program(program) == expected_output


def test_sixteen_digit():
    program = "1102,34915192,34915192,7,4,7,99,0"
    assert run_program(program) == [1219070632396864]


def test_large_number():
    program = "104,1125899906842624,99"
    assert run_program(program) == [1125899906842624]
