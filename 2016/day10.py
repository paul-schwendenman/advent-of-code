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

class Instruction(collections.namedtuple('Instruction', 'bot value')):
    __slots__ = ()


def parse_instructions(lines):
    robots: dict[int, tuple[int, int]] = {}
    instructions: list[Instruction] = []

    for line in lines:
        ints = extract_ints(line)
        if line[:5] == 'value':
            instructions.append(Instruction(ints[1], ints[0]))
            pass
        elif line[:3] == 'bot':
            m = re.match(r'bot \d+ gives low to (output|bot) \d+ and high to (output|bot) \d+', line)
            if not m:
                raise ValueError(m)

            low_key = ints[1] if m.group(1) == 'bot' else f'o{ints[1]}'
            high_key = ints[2] if m.group(2) == 'bot' else f'o{ints[2]}'
            robots[ints[0]] = (low_key, high_key)
            pass
        else:
            raise ValueError('Invalid instruction', line)

    return robots, instructions



def part1(data):
    robots, instructions = parse_instructions(data)
    values = collections.defaultdict(list)

    queue = collections.deque(instructions)

    # print(robots)
    print(instructions)

    while queue:
        instruction = queue.popleft()

        values[instruction.bot].append(instruction.value)

        if len(values[instruction.bot]) == 2:
            v = sorted(values[instruction.bot])

            low_bot = robots[instruction.bot][0]
            high_bot = robots[instruction.bot][1]

            for bot, value in [(low_bot, v[0]), (high_bot, v[1])]:
                queue.append(Instruction(bot, value))

    print(values)

    for key, value in values.items():
        if (s := sorted(value)) == [2, 5]:
            return key
        elif s == [17, 61]:
            return key
    pass


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
