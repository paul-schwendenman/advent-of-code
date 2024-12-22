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


def calc_next(secret, n=1):
    for _ in range(n):
        secret = (secret ^ (secret << 6)) % 16777216    # Multiply by 64, 64 = 2 ** 6
        secret = (secret ^ (secret >> 5)) % 16777216    # Divide by 32, 32 = 2 ** 5
        secret = (secret ^ (secret << 11 )) % 16777216  # Multiply by 2024, 2024 = 2 ** 11

    return secret


def part1(data):
    secrets = [int(line) for line in data]

    return sum(calc_next(secret, 2000) for secret in secrets)


def part2(data):
    secrets = [int(line) for line in data]
    changes_map = defaultdict(dict)

    for secret in secrets:
        changes = collections.deque(maxlen=4)
        price = secret % 10
        new_secret = secret

        for _ in range(2000):
            new_secret = calc_next(new_secret)
            new_price = new_secret % 10

            price_diff = new_price - price
            changes.append(price_diff)

            if len(changes) == 4 and secret not in changes_map[tuple(changes)]:
                changes_map[tuple(changes)][secret] = new_price

            price = new_price

    all_diffs = [sum(value.values()) for value in changes_map.values()]

    return max(all_diffs)


def main():
    # print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
