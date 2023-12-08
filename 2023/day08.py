import fileinput
import re
import itertools
import math
import functools
import collections

def parse_input(data):
    tree = {}

    instructions = list(next(data).strip())

    # burn a line
    next(data)

    for line in data:
        key, left, right = re.match(r'(\w+) = \((\w+), (\w+)\)', line).groups()
        tree[key] = {'L': left, 'R':right}

    return instructions, tree


def part1(data):
    instructions, tree = parse_input(data)

    instructions_loop = itertools.cycle(instructions)
    location = 'AAA'
    goal = 'ZZZ'

    step = 0
    while location != goal:
        instruction = next(instructions_loop)
        location = tree[location][instruction]
        step += 1

    return step


def part2(data):
    instructions, tree = parse_input(data)

    locations = [location for location in tree.keys() if location.endswith('A')]
    steps = [0] * len(locations)

    for index, _ in enumerate(locations):
        instructions_loop = itertools.cycle(instructions)

        while not locations[index].endswith('Z'):
            instruction = next(instructions_loop)
            locations[index] = tree[locations[index]][instruction]
            steps[index] += 1

    return math.lcm(*steps)


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
