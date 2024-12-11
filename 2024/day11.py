import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing

def extract_ints(string):
    return list(map(int, re.findall(r'-?\d+', string)))


def part1(data):
    line = [l for l in data][0]
    nums = extract_ints(line)
    new_nums = []

    for index in range(25):
        for n in nums:
            if n == 0:
                new_nums.append(1)
            elif (size := len(str(n))) % 2 == 0:
                half = size // 2
                front = int(str(n)[:half])
                back = int(str(n)[half:])
                new_nums.extend([front, back])
            else:
                new_nums.append(n * 2024)

        nums, new_nums = new_nums, []


    return len(nums)

    pass


@functools.lru_cache
def blink_stone(stone):
    if stone == 0:
        return [1]
    elif (size := len(str(stone))) % 2 == 0:
        half = size // 2
        front = int(str(stone)[:half])
        back = int(str(stone)[half:])

        return [front, back]
    else:
        return [stone * 2024]


def blink_stones(stone_counts):
    counts = collections.Counter()

    for stone, count in stone_counts.items():
        for new_stone in blink_stone(stone):
            counts[new_stone] += count

    return counts


def solve(line):
    nums = extract_ints(line)
    stone_counts = collections.Counter(nums)

    for _ in range(75):
        stone_counts = blink_stones(stone_counts)

    return sum(count for count in stone_counts.values())


def part2(data):
    line = [l for l in data][0]

    return solve(line)


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
