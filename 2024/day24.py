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


def get_int(gates, prefix='z'):
    number = [1 if gates.get(f'{prefix}{index:02d}', False) else 0 for index in range(99)]
    value = 0

    for digit in reversed(number):
        value = value << 1
        value += digit

    return value


def add_nums(gates, instructions):
    queue = collections.deque(instructions)
    instructions_map = {}

    while queue:
        instruction = queue.popleft()

        a, op, b, _, c = instruction.split(' ')

        if a not in gates or b not in gates:
            queue.append(instruction)
            continue

        instructions_map[c] = (op, a, b)

        if op == 'AND':
            gates[c] = gates[a] & gates[b]
            pass
        elif op == 'OR':
            gates[c] = gates[a] | gates[b]
            pass
        elif op == 'XOR':
            gates[c] = gates[a] ^ gates[b]
            pass
        else:
            raise ValueError(f'Invalid Op: {op}')

    return gates


def parse_data(data):
    initials, instructions = [chunk.strip().split('\n') for chunk in ''.join(data).split('\n\n')]
    pass

    gates: dict[str, bool] = {}

    for i in initials:
        name, value = i.split(': ')
        gates[name] = value == '1'

    return gates, instructions


def extract_operations(instructions):
    operations = {}

    for instruction in instructions:
        a, op, b, _, c = instruction.split(' ')
        operations[(op, a, b)] = c
        operations[(op, b, a)] = c

    return operations


def swap(instructions, n_bits=45):
    '''Swap outputs based on patterns

    half adder:
    X1 XOR Y1 => M1
    X1 AND Y1 => N1
    C0 AND M1 => R1
    C0 XOR M1 -> Z1
    R1 OR N1 -> C1
    '''
    operations = extract_operations(instructions)
    def find_operation(a, b, op):
        return operations.get((op, a, b), None)

    swapped = []
    c0 = None
    c1 = None

    for index in range(n_bits):
        number = f'{index:02d}'

        m1 = find_operation(f'x{number}', f'y{number}', 'XOR')
        n1 = find_operation(f'x{number}', f'y{number}', 'AND')

        if c0:
            r1 = find_operation(c0, m1, 'AND')
            if not r1:
                n1, m1 = m1, n1
                swapped.extend([n1, m1])
                r1 = find_operation(c0, m1, 'AND')

            z1 = find_operation(c0, m1, 'XOR')

            if m1[0] == 'z':
                m1, z1 = z1, m1
                swapped.extend([z1, m1])

            if n1[0] == 'z':
                n1, z1 = z1, n1
                swapped.extend([z1, n1])

            if r1[0] == 'z':
                r1, z1 = z1, r1
                swapped.extend([z1, r1])

            c1 = find_operation(r1, n1, 'OR')

        if c1 and c1[0] == 'z' and c1 != f'z{n_bits}':
            c1, z1 = z1, c1
            swapped.extend([c1, z1])

        if c0:
            c0 = c1
        else:
            c0 = n1

    return swapped


def part1(data):
    initial_gates, instructions = parse_data(data)

    gates = add_nums(initial_gates, instructions)

    return get_int(gates, 'z')


def part2(data):
    _, instructions = parse_data(data)

    return ','.join(sorted(swap(instructions)))


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
