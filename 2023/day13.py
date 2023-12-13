import fileinput
import re
import itertools
import math
import functools
import collections
import enum


def transpose(grid):
    return list(zip(*grid))


def extract_patterns(data):
    lines = ''.join(data)

    for chunk in lines.split('\n\n'):
        yield chunk.strip().split('\n')


def find_horizontal_reflection(pattern):
    for index, line in enumerate(pattern):
        before = list(reversed(pattern[:index]))
        after = pattern[index:]

        if len(before) == 0 or len(after) == 0:
            continue

        # print(f'{pattern=}')

        # print(f'{before=} {after=}')

        # print(f'{index:02}: {all(b == a for a, b in zip(before, after))} = {list(b == a for a, b in zip(before, after))}')
        if all(b == a for a, b in zip(before, after)):
            return index

        # for b, a in zip(before, after):
        #     print(f'{a=} {b=}')
        #     if b == a:
        #         pass
        #     else:
        #         continue
        # else:
        #     return index
    else:
        raise ValueError("No match found")


def count_diff(a, b):
    acc = 0
    for aa, bb in zip(a, b):
        if aa != bb:
            acc += 1

    return acc

def find_smugged_horizontal_reflection(pattern):
    for index, line in enumerate(pattern):
        before = list(reversed(pattern[:index]))
        after = pattern[index:]

        if len(before) == 0 or len(after) == 0:
            continue

        if sum(count_diff(a, b)for a, b in zip(before, after)) == 1:
            return index

    else:
        raise ValueError("No match found")


def find_vertical_reflection(pattern):
    return find_horizontal_reflection(transpose(pattern))

def find_smugged_vertical_reflection(pattern):
    return find_smugged_horizontal_reflection(transpose(pattern))


def part1(data):
    patterns = list(extract_patterns(data))

    print(f'{len(patterns)}')

    acc = 0

    for pattern in patterns:
        try:
            n = find_horizontal_reflection(pattern) * 100
            print(f'{n=}')
            acc += n
        except:
            pass
        finally:
            pass
        try:
            m = find_vertical_reflection(pattern)
            print(f'{m=}')
            acc += m
        except:
            pass
        finally:
            pass
    return acc




    pass


def part2(data):
    patterns = list(extract_patterns(data))

    print(f'{len(patterns)}')

    acc = 0

    for pattern in patterns:
        try:
            n = find_smugged_horizontal_reflection(pattern) * 100
            print(f'{n=}')
            acc += n
        except:
            pass
        finally:
            pass
        try:
            m = find_smugged_vertical_reflection(pattern)
            print(f'{m=}')
            acc += m
        except:
            pass
        finally:
            pass
    return acc
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
