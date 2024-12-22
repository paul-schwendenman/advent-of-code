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


def calc_next_secret(secret):
    secret = (secret ^ (secret << 6)) % 16777216    # Multiply by 64, 64 = 2 ** 6
    secret = (secret ^ (secret >> 5)) % 16777216    # Divide by 32, 32 = 2 ** 5
    secret = (secret ^ (secret << 11 )) % 16777216  # Multiply by 2024, 2024 = 2 ** 11

    return secret


def generate_secrets(secret):
    while True:
        yield (secret := calc_next_secret(secret))


def generate_prices(secret):
    calc_price = lambda secret: secret % 10

    yield from map(calc_price, generate_secrets(secret))


def calc_nth_secret(secret, n=1):
    *_, secret = itertools.islice(generate_secrets(secret), n)

    return secret


def part1(data):
    secrets = [int(line) for line in data]

    return sum(calc_nth_secret(secret, 2000) for secret in secrets)


def part2(data):
    secrets = [int(line) for line in data]
    changes_map = defaultdict(dict)

    for secret in secrets:
        rolling_diffs = collections.deque(maxlen=4)
        price = secret % 10

        for new_price in itertools.islice(generate_prices(secret), 2000):
            price_diff = new_price - price
            rolling_diffs.append(price_diff)
            frozen_diffs = tuple(rolling_diffs)

            if len(rolling_diffs) == 4 and secret not in changes_map[frozen_diffs]:
                changes_map[frozen_diffs][secret] = new_price

            price = new_price

    return max(sum(value.values()) for value in changes_map.values())


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
