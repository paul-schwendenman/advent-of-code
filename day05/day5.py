import sys
from enum import Enum


class Opcode(Enum):
    ADD = 1
    MULTIPY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF = 5
    JUMP_NOT_IF = 6
    LESS_THAN = 7
    EQUAL_TO = 8
    HALT = 99


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def parse_program(program):
    return (int(item) for item in program.split(','))


def split_instruction(instruction):
    opcode = Opcode(instruction % 100)
    instruction = list(str(instruction))
    parameter_modes = (["0"] * 5 + instruction)[-3:-6:-1]

    return opcode, parameter_modes


def lookup_value(memory, mode, position):
    try:
        if mode == '0':
            return memory[position]
        elif mode == '1':
            return position
    except IndexError:
        pass


def lookup_values(memory, parameter_modes, cursor):
    param_1 = lookup_value(memory, parameter_modes[0], cursor + 1)
    param_2 = lookup_value(memory, parameter_modes[1], cursor + 2)
    param_3 = lookup_value(memory, parameter_modes[2], cursor + 3)

    return param_1, param_2, param_3


def run_program(program, cursor=0, input_value=5):
    opcode, parameter_modes = split_instruction(program[cursor])

    params = lookup_values(program, parameter_modes, cursor)

    if opcode is Opcode.HALT:
        return program
    elif opcode is Opcode.ADD:
        program[params[2]] = program[params[0]] + program[params[1]]

        return run_program(program, cursor + 4, input_value)
    elif opcode is Opcode.MULTIPY:
        program[params[2]] = program[params[0]] * program[params[1]]

        return run_program(program, cursor + 4, input_value)
    elif opcode is Opcode.INPUT:
        program[params[0]] = input_value

        return run_program(program, cursor + 2, input_value)
    elif opcode is Opcode.OUTPUT:
        print(program[params[0]])

        return run_program(program, cursor + 2, input_value)
    elif opcode is Opcode.JUMP_IF:
        if program[params[0]]:
            return run_program(program, program[params[1]], input_value)

        return run_program(program, cursor + 3, input_value)
    elif opcode is Opcode.JUMP_NOT_IF:
        if not program[params[0]]:
            return run_program(program, program[params[1]], input_value)

        return run_program(program, cursor + 3, input_value)
    elif opcode is Opcode.LESS_THAN:
        program[params[2]] = 1 if program[params[0]] < program[params[1]] else 0

        return run_program(program, cursor + 4, input_value)
    elif opcode is Opcode.EQUAL_TO:
        program[params[2]] = 1 if program[params[0]] == program[params[1]] else 0

        return run_program(program, cursor + 4, input_value)
    else:
        print(f"missing opcode: {opcode}")


def main(param=1, filename='input'):
    with open(filename) as input_file:
        program_string = input_file.readlines()[0]

    program = list(parse_program(program_string))
    run_program(program, input_value=param)


if __name__ == "__main__":
    main(1)
    main(5)
