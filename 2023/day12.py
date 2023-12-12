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

        acc += count_arrangements2(springs + '.', sets)
    pass
    return acc


def extend_line(line):
    springs, sets = line.split(' ')

    new_springs = '?'.join([springs for _ in range(5)])
    new_sets = ','.join(sets for _ in range(5))

    return ' '.join([new_springs, new_sets])


@functools.cache
def count_arrangements2(springs, groups, index=0, spring_count=0, group_index=0):
    if index == len(springs):
        if len(groups) == group_index:
            return 1
        return 0
    elif springs[index] == '#':
        return count_arrangements2(springs, groups, index+1, spring_count+1, group_index)

    if springs[index] == '.' or group_index == len(groups):
        if group_index < len(groups) and spring_count == groups[group_index]:
            return count_arrangements2(springs, groups, index+1, 0, group_index+1)
        elif spring_count == 0:
            return count_arrangements2(springs, groups, index+1, 0, group_index)
        return 0

    elif springs[index] == '?':
        guess_broken_count = count_arrangements2(springs, groups, index+1, spring_count+1, group_index)

        guess_ok_count = 0

        if spring_count == groups[group_index]:
            guess_ok_count = count_arrangements2(springs, groups, index+1, 0, group_index+1)
        elif spring_count == 0:
            guess_ok_count = count_arrangements2(springs, groups, index+1, 0, group_index)

        return guess_broken_count + guess_ok_count


def part2(data):
    acc = 0

    for line in (data):
        springs, sets = parse_line(extend_line(line))

        acc += count_arrangements2(springs + '.', sets)

    return acc


def main():
    try:
        print(part1(fileinput.input()))
        print(part2(fileinput.input()))
    finally:
        print(f'cache: {count_arrangements2.cache_info()}')


if __name__ == '__main__':
    main()
