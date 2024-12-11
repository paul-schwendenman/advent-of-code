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

    print(f'nums: {nums}')


    for _ in range(25):
        # print('-------------')
        for n in nums:
            if n == 0:
                new_nums.append(1)
            elif (size := len(str(n))) % 2 == 0:
                half = size // 2
                front = int(str(n)[:half])
                back = int(str(n)[half:])
                # print(f'n: {n}\t f: {front}\t b: {back} s: {size} h: {half}')
                new_nums.append(front)
                new_nums.append(back)
            else:
                new_nums.append(n * 2024)

        # print(f'new:  {new_nums}')
        nums, new_nums = new_nums, []


    return len(nums)

    pass


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
