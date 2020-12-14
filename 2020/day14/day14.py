from __future__ import annotations
from typing import List
from aoc import readfile
from collections import defaultdict
import re


def convert_memory(value):
    return "{0:036b}".format(value)


def apply_mask_to_value(value, mask):
    value = convert_memory(value)
    return ''.join(a if b == 'X' else b for a, b in zip(value, mask))

def part1(data: List[str]) -> int:
    # memory = [0] * 37
    memory = defaultdict(int)
    mask = None
    for line in data:
        print(line)
        if line[:3] == 'mem':
            s = line.split('] = ')
            address = int(s[0].split('[')[1])
            value = int(s[1])
            print(address, value)
            print(convert_memory(value))
            print(apply_mask_to_value(value, mask))
            memory[address] = int(apply_mask_to_value(value, mask), base=2)
        else:
            mask = line[7:]
            print(mask)


    return sum(i[1] for i in memory.items())


def map_bit(bit, mask):
    if mask == '0':
        return bit
    elif mask == '1':
        return '1'
    elif mask == 'X':
        return 'X'


def apply_mask_to_address(address, mask):
    value = convert_memory(address)
    return ''.join(map_bit(a, b) for a, b in zip(value, mask))


def floating_addresses(address):
    if not address:
        return ['']
    # print(address[0], address[1:])
    if address[0] in '01':
        return [address[0] + part for part in floating_addresses(address[1:])]
    else:
        return ['1' + part for part in floating_addresses(address[1:])] +  ['0' + part for part in floating_addresses(address[1:])]


def part2(data: List[str]) -> int:
    # memory = [0] * 37
    memory = defaultdict(int)
    mask = None
    for line in data:
        print(line)
        if line[:3] == 'mem':
            s = line.split('] = ')
            address = int(s[0].split('[')[1])
            value = int(s[1])
            print(address, value)
            print(convert_memory(address))
            print(apply_mask_to_address(address, mask))
            for new_address in floating_addresses(apply_mask_to_address(address, mask)):
                memory[new_address] = value

            # memory[address] = int(apply_mask_to_value(value, mask), base=2)
        else:
            mask = line[7:]
            print(mask)


    return sum(i[1] for i in memory.items())
    pass


def main() -> None:
    with readfile() as data:
        # print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
