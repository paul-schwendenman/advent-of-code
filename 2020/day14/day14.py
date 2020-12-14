from __future__ import annotations
from typing import List
from aoc import readfile
from collections import defaultdict
import re


def convert_memory(value):
    return "{0:036b}".format(value)


def apply_mask(value, mask):
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
            print(apply_mask(value, mask))
            memory[address] = int(apply_mask(value, mask), base=2)
        else:
            mask = line[7:]
            print(mask)


    return sum(i[1] for i in memory.items())


def part2(data: List[str]) -> int:
    pass


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
