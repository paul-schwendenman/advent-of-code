import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing
import hashlib
from utils import *


def part1(data):
    door_id = [line.rstrip() for line in data][0]

    password = ''
    index = 0

    for _ in range(8):
        while not (hashed := hashlib.md5((door_id + str(index)).encode('utf-8')).hexdigest()).startswith('00000'):
            index += 1
        password += hashed[5]
        index += 1

    return password


def part2(data):
    door_id = [line.rstrip() for line in data][0]

    password = {}
    index = 0

    while len(password.keys()) < 8:
        while not (hashed := hashlib.md5((door_id + str(index)).encode('utf-8')).hexdigest()).startswith('00000'):
            index += 1
        position = int(hashed[5], base=16)
        value = hashed[6]

        if 0 <= position < 8:
            password[position] = value
            print('\r' + ''.join(password.get(i, ' ') for i in range(8)), end='')

        index += 1

    print('\r')

    return ''.join(password[i] for i in range(8))


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
