import fileinput
import re
import itertools
import math
import functools
import collections

def part1(data):
    tree = {}

    instructions = list(next(data).strip())
    print(f'{instructions=}')
    instructions_loop = itertools.cycle(instructions)

    next(data)

    for line in data:
        # key, left, right = re.match(r'([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)', line).groups()
        key, left, right = re.match(r'([A-Z0-9]+) = \(([A-Z0-9]+), ([A-Z0-9]+)\)', line).groups()
        tree[key] = (left, right)
        pass

    print(f'{tree=}')


    location = 'AAA'
    goal = 'ZZZ'

    step = 0
    while location != goal:
        instruction = next(instructions_loop)
        code = 0 if instruction == 'L' else 1
        print(f'{instruction=} {location=}')
        location = tree[location][code]
        step += 1

        # if step > 3:
            # break

    return step
    pass


def lcm(*vals):
    print(vals)
    lcm = vals[0]
    for next_val in vals[1:]:
        lcm = lcm * next_val // math.gcd(lcm, next_val)

    return lcm

def part2(data):
    tree = {}

    instructions = list(next(data).strip())
    print(f'{instructions=}')

    next(data)

    for line in data:
        key, left, right = re.match(r'([A-Z0-9]+) = \(([A-Z0-9]+), ([A-Z0-9]+)\)', line).groups()
        tree[key] = (left, right)
        pass

    print(f'{tree=}')

    starts = [location for location in tree.keys() if location.endswith('A')]


    locations = starts

    steps = [0] * len(locations)

    for i, location in enumerate(locations):
        instructions_loop = itertools.cycle(instructions)
        step = 0

        while not locations[i].endswith('Z'):
            instruction = next(instructions_loop)
            code = 0 if instruction == 'L' else 1
            # print(f'{instruction=} {location=}')
            locations[i] = tree[locations[i]][code]
            step += 1

        steps[i] = step


        # if step > 3:
            # break
    print(f'{steps=}')

    return lcm(*steps)
    pass

def main():
    # print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
