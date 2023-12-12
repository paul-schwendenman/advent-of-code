import fileinput
import re
import itertools
import math
import functools
import collections
import enum
from tqdm import tqdm

def parse_line(line):
    springs, sets = line.split(' ')
    # springs = springs.split('')
    sets = tuple(int(item) for item in sets.split(','))

    return springs, sets


def generate_permutations(springs):
    if not springs:
        yield ()
    else:
        spring = springs[0]

        for past in generate_permutations(springs[1:]):
            if spring == '.' or spring == '#':
                yield (spring,) + past
            elif spring == '?':
                yield ('.',) + past
                yield ('#',) + past
            else:
                raise ValueError('Invalid spring type')


def count_arrangements(springs, sets):
    acc = 0
    for permutation in generate_permutations(springs):
        if score_springs(permutation) == sets:
            acc += 1

    return acc


def score_springs(springs):
    sets = tuple()
    count = 0

    for spring in springs:
        # print(f'{spring} {count=} {sets}')
        if spring == '#':
            count += 1
        elif spring == '.':
            if count > 0:
                sets = sets + (count,)
            count = 0
    else:
        if count > 0:
            sets = sets + (count,)
    return sets

def part1(data):
    acc = 0

    for line in data:
        springs, sets = parse_line(line)

        acc += count_arrangements(springs, sets)
    pass
    return acc


def extend_line(line):
    springs, sets = line.split(' ')

    new_springs = '?'.join([springs for _ in range(5)])
    new_sets = ','.join([sets for _ in range(5)])

    return ' '.join([new_springs, new_sets])



def part2(data):
    acc = 0

    for line in tqdm(data):
        springs, sets = parse_line(extend_line(line))

        acc += count_arrangements(springs, sets)
    pass
    return acc
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
