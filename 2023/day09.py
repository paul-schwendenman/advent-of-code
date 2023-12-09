import fileinput
import re
import itertools
import math
import functools
import collections

def solve(seq):
    print(f'{seq=}')
    if all(map(lambda item: item == 0, seq)):
        print(f'out={seq + [0]}')
        return seq + [0]

    else:
        nxt = [b - a for a, b in itertools.pairwise(seq)]

        v = solve(nxt)
        print(f'{v=}')

        # print(f'{nxt[-1]} + {v} = {nxt[-1] + v}')

        out =  seq[:] + [seq[-1] + v[-1]]
        print(f'{out=}')
        return out


def solve2(seq):
    print(f'{seq=}')
    if all(map(lambda item: item == 0, seq)):
        print(f'out={seq + [0]}')
        return seq + [0]

    else:
        nxt = [b - a for a, b in itertools.pairwise(seq)]

        v = solve2(nxt)
        print(f'{v=}')

        # print(f'{nxt[-1]} + {v} = {nxt[-1] + v}')

        out =  [seq[0] - v[0]] + seq[:]
        print(f'{out=}')
        return out


def part1(data):
    acc = 0

    for line in data:
        seq = [int(item) for item in line.split(' ')]

        acc += solve(seq)[-1]

    return acc

def part2(data):
    acc = 0

    for line in data:
        seq = [int(item) for item in line.split(' ')]

        acc += solve2(seq)[0]

    return acc
    pass

def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
