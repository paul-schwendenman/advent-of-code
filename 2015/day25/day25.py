import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing


def generate_next_number(number = 20151125):
    return (number * 252533) % 33554393


def convert_coords(row, col):
    '''
    0, 0
    0, 1
    1, 0
    0, 2
    1, 1
    2, 0
    0, 3
    1, 2
    2, 1
    3, 0
    '''
    x, y = 1, 1
    count = 1
    max_y = 1

    while True:
    # for _ in range(20):
        # print(f'n: {count:3d} col: {x:3d} row: {y:3d}')
        if x == col and y == row:
            return count
        new_y = y - 1
        new_x = x + 1

        if new_y == 0:
            new_x = 1
            new_y = max_y + 1
            max_y += 1

        x, y = new_x, new_y
        count += 1


def find_nth(nth):
    number = 20151125

    for _ in range(nth - 1):
        number = generate_next_number(number)

    return number


def find_row_col(row, col):
    nth = convert_coords(row, col)

    return find_nth(nth)


def extract_ints(string):
    return list(map(int, re.findall(r'-?\d+', string)))

def part1(data):
    row, col = [extract_ints(line) for line in data][0]

    print(row, col)

    return find_row_col(row, col)


def part2(data):
    pass


def main():
    assert generate_next_number() == 31916031
    assert convert_coords(1,1) == 1
    assert convert_coords(3,3) == 13
    assert find_nth(12) == 32451966, f'{find_nth(12)} == 32451966'
    assert find_nth(13) == 1601130
    assert find_nth(14) == 7726640
    assert find_row_col(6, 6) == 27995004, f'{find_row_col(6, 6)} == 27995004'
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
