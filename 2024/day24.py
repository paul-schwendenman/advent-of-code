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


def follow_path(gates: dict[str, tuple[str, str, str]], goal: str):
    if goal.startswith('x'):
        return goal
    elif goal.startswith('y'):
        return goal

    op, a, b = gates[goal]

    return f'({follow_path(gates, a)}) {op} ({follow_path(gates, b)})'


def part1(data):
    initials, instructions = [chunk.strip().split('\n') for chunk in ''.join(data).split('\n\n')]
    pass

    gates: dict[str, bool] = {}

    for i in initials:
        name, value = i.split(': ')
        gates[name] = value == '1'

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

    x = (get_int(gates, 'x'))
    y = (get_int(gates, 'y'))
    z = (get_int(gates, 'z'))

    print(f'{x:46b} = {x}')
    print(f'{y:46b} = {y}')
    print('-' * 50)
    print(f'{x+y:46b} = {x+y} = {x} + {y}')
    print(f'{z:b} = {z}')

    print(f'{(x+y) ^ z:46b}')

    # for i in range(46):
    #     z = f'z{i:02d}'
    #     print(f'{z} = {follow_path(instructions_map, z)}')

    return z
    z = [1 if gates.get(f'z{index:02d}', False) else 0 for index in range(99)]
    print(z)

    value = 0

    for digit in reversed(z):
        value = value << 1
        value += digit

    return value


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
