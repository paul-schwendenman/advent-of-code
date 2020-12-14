from __future__ import annotations
from typing import List
from aoc import readfile
from collections import defaultdict


def convert_memory(value: int) -> str:
    return "{0:036b}".format(value)


def apply_mask_to_value(value: int, mask: str) -> str:
    new_value = convert_memory(value)
    return ''.join(a if b == 'X' else b for a, b in zip(new_value, mask))


def part1(data: List[str]) -> int:
    # memory = [0] * 37
    memory = defaultdict(int)
    mask = None
    for line in data:
        if line[:3] == 'mem':
            s = line.split('] = ')
            address = int(s[0].split('[')[1])
            value = int(s[1])
            memory[address] = int(apply_mask_to_value(value, mask), base=2)
        else:
            mask = line[7:]

    return sum(i[1] for i in memory.items())


def map_bit(bit: str, mask: str) -> str:
    if mask == '0':
        return bit
    elif mask == '1':
        return '1'
    elif mask == 'X':
        return 'X'
    raise ValueError('Expected 1, 0, or X')


def apply_mask_to_address(address: int, mask: str) -> str:
    value = convert_memory(address)
    return ''.join(map_bit(a, b) for a, b in zip(value, mask))


def floating_addresses(address: str) -> List[str]:
    if not address:
        return ['']
    if address[0] in '01':
        return [address[0] + part for part in floating_addresses(address[1:])]
    else:
        return ['1' + part for part in floating_addresses(address[1:])] +  ['0' + part for part in floating_addresses(address[1:])]


def part2(data: List[str]) -> int:
    # memory = [0] * 37
    memory = defaultdict(int)
    mask = ''
    for line in data:
        if line[:3] == 'mem':
            s = line.split('] = ')
            address = int(s[0].split('[')[1])
            value = int(s[1])
            for new_address in floating_addresses(apply_mask_to_address(address, mask)):
                memory[new_address] = value
        else:
            mask = line[7:]

    return sum(i[1] for i in memory.items())


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
