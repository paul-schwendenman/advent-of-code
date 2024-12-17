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

def run_program(reg_a, reg_b, reg_c, instructions, goal=None):
    cursor = 0
    output = []

    while cursor < len(instructions):
        instruction = instructions[cursor]
        operand = instructions[cursor + 1]
        jump = 2

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
                reg_b = reg_b ^ operand
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
                reg_b = reg_c ^ reg_b
            case 5, 0 | 1 | 2 | 3:
                output.append(operand % 8)
                if goal:
                    if len(output) > len(goal):
                        break
                    if goal[:len(output)] != output:
                        break
            case 5, 4:
                output.append(reg_a % 8)
                if goal:
                    if len(output) > len(goal):
                        break
                    if goal[:len(output)] != output:
                        break
            case 5, 5:
                output.append(reg_b % 8)
                if goal:
                    if len(output) > len(goal):
                        break
                    if goal[:len(output)] != output:
                        break
            case 5, 6:
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

        cursor += jump
    return output


def part1(data):
    lines = [extract_ints(line) for line in data]

    instructions = lines[-1]
    reg_a = lines[0][0]
    reg_b = lines[1][0]
    reg_c = lines[2][0]

    output = run_program(reg_a, reg_b, reg_c, instructions)

    return ','.join(map(str, output))


def get_output(a):
    return ((((a % 8) ^ 1) ^ (a >> ((a % 8) ^ 1))) ^ 4) % 8


def run(a):
    outs = []

    while a > 0:
        outs.append(get_output(a))
        a = a >> 3

    return ','.join(map(str, outs))


def solve(program, a):
    meta_inputs = { 0 }

    for num in reversed(program):
        new_meta_inputs = set()

        for current_number in meta_inputs:
            for new_segment in range(8):
                new_number = (current_number << 3) + new_segment

                if get_output(new_number) == num:
                    new_meta_inputs.add(new_number)

        meta_inputs = new_meta_inputs

    return run(a), min(meta_inputs)


def part2(data):
    lines = [extract_ints(line) for line in data]

    instructions = lines[-1]
    reg_a = lines[0][0]

    return solve(instructions, reg_a)[1]


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
