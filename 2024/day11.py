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

    for _ in range(25):
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


@functools.cache
def blink_stone(stone):
    if stone == 0:
        return [1]
    elif (size := len(s_stone := str(stone))) % 2 == 0:
        half = size // 2
        front = int(s_stone[:half])
        back = int(s_stone[half:])

        return [front, back]
    else:
        return [stone * 2024]


def blink_stones(stone_counts):
    new_counts = collections.Counter()

    for stone, count in stone_counts.items():
        for new_stone in blink_stone(stone):
            new_counts[new_stone] += count

    return new_counts


def solve(line, n=75):
    nums = extract_ints(line)
    stone_counts = collections.Counter(nums)

    for _ in range(n):
        stone_counts = blink_stones(stone_counts)

    return stone_counts.total()


def part2(data):
    line = [l for l in data][0]

    return solve(line, 75)


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))
    try:
        print(blink_stone.cache_info())
    except:
        pass


if __name__ == '__main__':
    main()
