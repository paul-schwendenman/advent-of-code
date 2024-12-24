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
    initials, instructions = [chunk.strip().split('\n') for chunk in ''.join(data).split('\n\n')]
    pass

    gates: dict[str, bool] = {}

    for i in initials:
        name, value = i.split(': ')
        gates[name] = value == '1'

    print(gates)
    queue = collections.deque(instructions)

    while queue:
        instruction = queue.popleft()

    # for instruction in instructions:
        a, op, b, _, c = instruction.split(' ')

        if a not in gates or b not in gates:
            queue.append(instruction)
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

    z = [1 if gates.get(f'z{index:02d}', False) else 0 for index in range(99)]
    print(z)

    value = 0

    for digit in reversed(z):
        value = value << 1
        value += digit

    return value


    return








def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
