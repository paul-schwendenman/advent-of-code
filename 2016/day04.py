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


class Room(collections.namedtuple('Room', 'encrypted_name sector_id checksum valid name')):
    __slots__ = ()


def calc_checksum(encrypted_name):
    key = lambda item: (-item[1], item[0])
    c = collections.Counter(encrypted_name)
    del c['-']
    pairs = c.most_common()

    return ''.join(pair[0] for pair in sorted(pairs, key=key))[:5]


def decrypt_name(encrypted_name, sector_id):
    def d(c):
        if c == '-':
            return ' '

        return chr(((ord(c) - ord('a') + sector_id) % 26) + ord('a'))
        pass

    return ''.join(d(c) for c in encrypted_name)


def check_room(line):
    match = re.match(r'([a-z-]+)-([0-9]+)(?:\[([a-z]+)\])?', line)
    encrypted_name, sector, checksum = match.groups()
    sector_id = int(sector)

    valid = checksum == calc_checksum(encrypted_name)
    name = decrypt_name(encrypted_name, sector_id)

    return Room(encrypted_name, sector_id, checksum, valid, name)


def part1(data):
    rooms = [check_room(line) for line in data]

    return sum(room.sector_id for room in rooms if room.valid)


def part2(data):
    rooms = [check_room(line) for line in data]

    try:
        return [room for room in rooms if 'north' in room.name][0].sector_id
    except:
        pass



def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
