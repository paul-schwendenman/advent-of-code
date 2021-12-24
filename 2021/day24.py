import fileinput
from itertools import cycle, product
from collections import Counter, namedtuple
from typing import MutableMapping, Tuple
from enum import Enum

def run_program(program, inputs):
    variables = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }

    for line in program:
        [cmd, *args] = line.split(' ')

        if len(args) == 2:
            if args[1] in 'wxyz':
                b = variables[args[1]]
            else:
                b = int(args[1])

        if cmd == 'inp':
            assert len(args) == 1

            try:
                variables[args[0]] = int(next(inputs))
            except StopIteration:
                # print(variables)
                return(variables)
            pass

        elif cmd == 'add':
            assert len(args) == 2

            variables[args[0]] += b

        elif cmd == 'mul':
            variables[args[0]] *= b
            pass

        elif cmd == 'div':
            variables[args[0]] //= b
            pass

        elif cmd == 'mod':
            variables[args[0]] %= b
            pass

        elif cmd == 'eql':
            variables[args[0]] = 1 if variables[args[0]] == b else 0

        else:
            raise ValueError(f'Invalid command: {cmd}')

    return variables

def check_model_number(number):
    return all(char != '0' for char in str(number))

def convert_model_number(number):
    string = str(number)

    for char in string:
        yield int(char)


def part1(data) -> int:

    # print(run_program(data, inputs=convert_model_number(13_579_246_899_999)))

    # for i in range(99_999_999_999_999, 0, -1):
    for i in range(49_999_999_999_999, 0, -1):
        if i % 10_000 == 0:
            print(i)
        if not check_model_number(i):
            # print(f'skipping {i}')
            continue

        inputs = convert_model_number(i)

        variables = run_program(data, inputs)

        if variables['z'] == 0:
            return i


    pass


def part2(data) -> int:
    pass


def main():
    with fileinput.input() as input:
        data = [line.rstrip() for line in input]

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
