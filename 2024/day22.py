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

def calc_next(secret):
    secret = (secret ^ (secret << 6)) % 16777216
    secret = (secret ^ (secret >> 5)) % 16777216
    secret = (secret ^ (secret << 11 )) % 16777216
    return secret


def part1(data):
    acc = 0
    for line in data:
        secret = int(line)
        new_secret = secret
        for _ in range(2000):
            new_secret = calc_next(new_secret)

        acc += new_secret
        print(f'{secret}: {new_secret}')

    return acc


    pass


def part2(data):
    acc = 0
    changes_map = defaultdict(dict)

    for line in data:
        changes = collections.deque(maxlen=4)
        secret = int(line)
        price = secret % 10
        new_secret = secret
        # print(f'{secret:10d}: {price}')
        for _ in range(2000):
        # for _ in range(10 - 1):
            new_secret = calc_next(new_secret)
            new_price = new_secret % 10

            price_diff = new_price - price
            changes.append(price_diff)

            # print(f'{new_secret:10d}: {new_price} ({price_diff}) {tuple(changes)}')

            if len(changes) == 4 and secret not in changes_map[tuple(changes)]:
                changes_map[tuple(changes)][secret] = new_price
            pass

            price = new_price

        acc += new_secret
        # print(f'{secret}: {new_secret}')

    all_diffs = [sum(value.values()) for key, value in changes_map.items()]
    # pprint.pprint(all_diffs)
    # pprint.pprint(changes_map)
    pprint.pprint(changes_map[(-2,1,-1,3)])

    return max(all_diffs)
    pass


def main():
    # print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
