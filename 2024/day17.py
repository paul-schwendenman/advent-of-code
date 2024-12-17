import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing
from utils import *


def part1(data):
    lines = [extract_ints(line) for line in data]
    reg_a = lines[0][0]
    reg_b = lines[1][0]
    reg_c = lines[2][0]

    cursor = 0
    instructions = lines[-1]
    output = []

    print(reg_a, reg_b, reg_c)
    print(instructions)

    while cursor < len(instructions):
        instruction = instructions[cursor]
        operand = instructions[cursor + 1]
        jump = 2
        print(f'curs: {cursor}\t inst: {instruction}\t oper: {operand}')
        print(f'reg_a: {reg_a}, reg_b: {reg_b}, reg_c: {reg_c}')
        match instruction, operand:
            case 0, 0 | 1 | 2 | 3:
                reg_a = reg_a // ( 2 ** operand)
            case 0, 4:
                reg_a = reg_a // ( 2 ** reg_a)
            case 0, 5:
                reg_a = reg_a // ( 2 ** reg_b)
            case 0, 6:
                reg_a = reg_a // ( 2 ** reg_c)
            case 1, _:
                reg_b = reg_b | operand
            case 2, 0 | 1 | 2 | 3:
                reg_b = operand % 8
            case 2, 4:
                reg_b = reg_a % 8
            case 2, 5:
                reg_b = reg_b % 8
            case 2, 6:
                reg_b = reg_c % 8
            case 3, _:
                if not reg_a == 0:
                    cursor = operand
                    jump = 0

            case 4, _:
                reg_b = reg_c | reg_b
            case 5, 0 | 1 | 2 | 3:
                # print(f'{operand % 8},', end='')
                output.append(operand % 8)
            case 5, 4:
                # print(f'{reg_a % 8},', end='')
                output.append(reg_a % 8)
            case 5, 5:
                # print(f'{reg_b % 8},', end='')
                output.append(reg_b % 8)
            case 5, 6:
                # print(f'{reg_c % 8},', end='')
                output.append(reg_c % 8)
            case 6, 0 | 1 | 2 | 3:
                reg_b = reg_a // ( 2 ** operand)
            case 6, 4:
                reg_b = reg_a // ( 2 ** reg_a)
            case 6, 5:
                reg_b = reg_a // ( 2 ** reg_b)
            case 6, 6:
                reg_b = reg_a // ( 2 ** reg_c)
            case 7, 0 | 1 | 2 | 3:
                reg_c = reg_a // ( 2 ** operand)
            case 7, 4:
                reg_c = reg_a // ( 2 ** reg_a)
            case 7, 5:
                reg_c = reg_a // ( 2 ** reg_b)
            case 7, 6:
                reg_c = reg_a // ( 2 ** reg_c)
            case _:
                raise ValueError('Missing opcode:', instruction, operand, cursor)

        print(f'reg_a: {reg_a}, reg_b: {reg_b}, reg_c: {reg_c}')
        print(f'jump: {jump}')
        print(f'out: {output}')
        # input()
        cursor += jump
    return ','.join(map(str, output))

    pass


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
