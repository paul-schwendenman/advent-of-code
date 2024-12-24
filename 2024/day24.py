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


def get_list(gates, prefix='z'):
    return [1 if gates.get(f'{prefix}{index:02d}', False) else 0 for index in range(99)]

def get_int(gates, prefix='z'):
    number = [1 if gates.get(f'{prefix}{index:02d}', False) else 0 for index in range(99)]
    value = 0

    for digit in reversed(number):
        value = value << 1
        value += digit

    return value


def follow_path(gates: dict[str, tuple[str, str, str]], goal: str, depth=3):
    if depth == 0:
        return f'{goal}:...'
    if goal.startswith('x'):
        return goal
    elif goal.startswith('y'):
        return goal

    op, a, b = gates[goal]

    return f'{goal} := ({follow_path(gates, a, depth-1)}) {op} ({follow_path(gates, b, depth-1)})'


def add_nums(gates, instructions):
    queue = collections.deque(instructions)
    instructions_map = {}

    while queue:
        instruction = queue.popleft()

    # for instruction in instructions:
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

    return [1 if gates.get(f'z{index:02d}', False) else 0 for index in range(99)]


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


def part1(data):
    initials, instructions = [chunk.strip().split('\n') for chunk in ''.join(data).split('\n\n')]
    gates: dict[str, bool] = {}

    for i in initials:
        name, value = i.split(': ')
        gates[name] = value == '1'

    queue = collections.deque(instructions)

    while queue:
        instruction = queue.popleft()

        a, op, b, _, c = instruction.split(' ')

        if a not in gates or b not in gates:
            queue.append(instruction)
            continue

        if op == 'AND':
            gates[c] = gates[a] & gates[b]
        elif op == 'OR':
            gates[c] = gates[a] | gates[b]
        elif op == 'XOR':
            gates[c] = gates[a] ^ gates[b]
        else:
            raise ValueError(f'Invalid Op: {op}')

    return get_int(gates, 'z')


def find_instruction(instructions: list[str], a: str, b: str, op: str):
    for instruction in instructions:
        if instruction.startswith(f'{a} {op} {b}') or instruction.startswith(f'{b} {op} {a}'):
            return instruction.split(' -> ')[1]


def swap(instructions, n_bits=45):
    '''Swap outputs based on patterns

    half adder:
    X1 XOR Y1 => M1
    X1 AND Y1 => N1
    C0 AND M1 => R1
    C0 XOR M1 -> Z1
    R1 OR N1 -> C1
    '''
    swapped = []
    c0 = None
    c1 = None

    for index in range(n_bits):
        number = f'{index:02d}'

        m1 = find_instruction(instructions, f'x{number}', f'y{number}', 'XOR')
        n1 = find_instruction(instructions, f'x{number}', f'y{number}', 'AND')

        if c0:
            r1 = find_instruction(instructions, c0, m1, 'AND')
            if not r1:
                n1, m1 = m1, n1
                swapped.extend([n1, m1])
                r1 = find_instruction(instructions, c0, m1, 'AND')

            z1 = find_instruction(instructions, c0, m1, 'XOR')

            if m1.startswith('z'):
                m1, z1 = z1, m1
                swapped.extend([z1, m1])

            if n1.startswith('z'):
                n1, z1 = z1, n1
                swapped.extend([z1, n1])

            if r1.startswith('z'):
                r1, z1 = z1, r1
                swapped.extend([z1, r1])

            c1 = find_instruction(instructions, r1, n1, 'OR')

        if c1 and c1.startswith('z') and c1 != f'z{n_bits}':
            c1, z1 = z1, c1
            swapped.extend([c1, z1])

        if c0:
            c0 = c1
        else:
            c0 = n1

    return swapped


def part2(data):
    _, instructions = parse_data(data)

    return ','.join(sorted(swap(instructions)))


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
