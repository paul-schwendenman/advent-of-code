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
        return goal
    if goal.startswith('x'):
        return goal
    elif goal.startswith('y'):
        return goal

    op, a, b = gates[goal]

    return f'({follow_path(gates, a, depth-1)}) {op} ({follow_path(gates, b, depth-1)})'


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

def add_nums2(gates, instructions):
    queue = collections.deque(instructions.keys())

    while queue:
        c = queue.popleft()

    # for instruction in instructions:
        op, a, b = instructions[c]

        if a not in gates or b not in gates:
            queue.append(c)
            continue

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

    return [1 if gates.get(f'z{index:02d}', False) else 0 for index in range(98, -1, -1)]


def parse_data(data):
    initials, instructions = [chunk.strip().split('\n') for chunk in ''.join(data).split('\n\n')]
    pass

    gates: dict[str, bool] = {}

    for i in initials:
        name, value = i.split(': ')
        gates[name] = value == '1'

    return gates, instructions


def map_instructions(instructions):
    outs = {}

    for instruction in instructions:
        a, op, b, _, c = instruction.split(' ')
        outs[c] = (op, a, b)

    return outs


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

def score_nums(a, b):
    count = 0
    for i, j in reversed(list(zip(a, b))):
        if i == j:
            count += 1
        else:
            break

    return count



def part2(data):
    gates, instructions = parse_data(data)

    x = (get_int(gates, 'x'))
    y = (get_int(gates, 'y'))
    goal_z = [int(item) for item in f'{x+y:099b}']
    z = add_nums(gates, instructions)

    # print(z)
    # print(goal_z)
    # print(len(z), len(goal_z))
    # print(score_nums(z, goal_z))
    # print(score_nums(z, z))

    outs = map_instructions(instructions)

    z2 = add_nums2(gates, outs)
    score = (score_nums(z2, goal_z))

    for a, b in itertools.combinations(outs.keys(), r=8):
        outs[a], outs[b] = outs[b], outs[a]

        z3 = add_nums2(gates, outs)

        if (score_nums(z3, goal_z)) > score:
            print(a, b)

        outs[a], outs[b] = outs[b], outs[a]
        pass

    z2 = add_nums2(gates, outs)

    # print(len(z2), len(goal_z))
    # print(z2)
    # print(score_nums(z2, goal_z))

    # assert z == list(reversed(z2))


    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
