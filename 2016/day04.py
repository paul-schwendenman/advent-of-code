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


class Room(collections.namedtuple('Room', 'encrypted_name sector_id checksum valid')):
    __slots__ = ()


def calc_checksum(encrypted_name):
    key = lambda item: (-item[1], item[0])
    c = collections.Counter(encrypted_name)
    del c['-']
    pairs = c.most_common()

    return ''.join(pair[0] for pair in sorted(pairs, key=key))[:5]


def check_room(line):
    match = re.match(r'([a-z-]+)-([0-9]+)\[([a-z]+)\]', line)
    encrypted_name, sector_id, checksum = match.groups()

    valid = checksum == calc_checksum(encrypted_name)

    return Room(encrypted_name, int(sector_id), checksum, valid)


def part1(data):
    rooms = [check_room(line) for line in data]

    return sum(room.sector_id for room in rooms if room.valid)


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
