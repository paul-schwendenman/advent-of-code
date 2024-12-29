import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing


def parse_program(data: typing.Iterator[str]):
    instructions = []
    for line in data:
        opcode, *parts = line.split()
        if opcode == 'hlf':
            instructions.append(('hlf', parts[0]))
        elif opcode == 'tpl':
            instructions.append(('tpl', parts[0]))
        elif opcode == 'inc':
            instructions.append(('inc', parts[0]))
        elif opcode == 'jmp':
            instructions.append(('jmp', int(parts[0]) ))
        elif opcode == 'jie':
            instructions.append(('jie', parts[0][0], int(parts[1])))
        elif opcode == 'jio':
            instructions.append(('jio', parts[0][0], int(parts[1]) ))
        else:
            raise ValueError(f'Invalid line: {line}')

    return instructions


def run_program(instructions, reg_a, reg_b, cursor=0):
    while cursor < len(instructions):
        opcode, *args = instructions[cursor]
        print(f'{cursor:2d}. reg_a={reg_a}\t reg_b={reg_b}\t {opcode} {args}')
        jump = 1

        match opcode, args[0]:
            case 'hlf', 'a':
                print(f'{reg_a} {reg_a >> 1}')
                reg_a = reg_a >> 1

            case 'hlf', 'b':
                reg_b = reg_b >> 1

            case 'tpl', 'a':
                reg_a = reg_a * 3

            case 'tpl', 'b':
                reg_b = reg_b * 3

            case 'inc', 'a':
                reg_a += 1

            case 'inc', 'b':
                reg_b += 1

            case 'jmp', _:
                jump = args[0]

            case 'jie', 'a':
                if reg_a % 2 == 0:
                    jump = args[1]

            case 'jie', 'b':
                if reg_b % 2 == 0:
                    jump = args[1]

            case 'jio', 'a':
                if reg_a == 1:
                    jump = args[1]

            case 'jio', 'b':
                if reg_b == 1:
                    jump = args[1]

            case _:
                raise ValueError(f'{opcode}')


        print(f'{cursor:2d}. reg_a={reg_a}\t reg_b={reg_b} going to {cursor + jump}')
        cursor += jump
    return reg_a, reg_b



def part1(data):
    instructions = parse_program(data)

    # pprint.pprint(instructions)

    return run_program(instructions, 0, 0)
    pass


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
