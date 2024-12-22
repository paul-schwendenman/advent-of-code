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


def make_sequence(secret, n=1):
    yield from itertools.islice(generate_secrets(secret), n)


def calc_sequence(secret, n=1):
    for _ in range(n):
        secret = calc_next_secret(secret)

    return secret


def part1(data):
    secrets = [int(line) for line in data]

    return sum(calc_sequence(secret, 2000) for secret in secrets)


def part2(data):
    secrets = [int(line) for line in data]
    changes_map = defaultdict(dict)

    for secret in secrets:
        changes = collections.deque(maxlen=4)
        price = secret % 10

        for new_price in itertools.islice(generate_prices(secret), 2000):
            price_diff = new_price - price
            changes.append(price_diff)

            if len(changes) == 4 and secret not in changes_map[tuple(changes)]:
                changes_map[tuple(changes)][secret] = new_price

            price = new_price

    all_diffs = [sum(value.values()) for value in changes_map.values()]

    return max(all_diffs)


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
