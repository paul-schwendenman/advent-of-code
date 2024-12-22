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
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
