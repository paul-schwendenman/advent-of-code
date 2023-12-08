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

def part2(data):
    tree = {}

    instructions = list(next(data).strip())
    print(f'{instructions=}')
    instructions_loop = itertools.cycle(instructions)

    next(data)

    for line in data:
        key, left, right = re.match(r'([A-Z0-9]+) = \(([A-Z0-9]+), ([A-Z0-9]+)\)', line).groups()
        tree[key] = (left, right)
        pass

    print(f'{tree=}')

    starts = [location for location in tree.keys() if location.endswith('A')]


    locations = starts

    step = 0
    while any(map(lambda item: not item.endswith('Z'), locations)):
        instruction = next(instructions_loop)
        code = 0 if instruction == 'L' else 1
        # print(f'{instruction=} {location=}')
        for i, location in enumerate(locations):
            locations[i] = tree[location][code]
        step += 1


        if any(map(lambda item: item.endswith('Z'), locations)):
            print(f'{step=}: {locations=}')

        # if step > 3:
            # break

    return step
    pass

def main():
    # print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
