import fileinput
from helper import *

def to_snafu(number):
    digits = {0: '0', 1: '1', 2: '2', -2: '=', -1: '-' }

    if number == 0:
        return ''

    remainder = (number + 2) % 5 - 2
    quotient = (number + 2) // 5

    return to_snafu(quotient) + digits[remainder]


def from_snafu(number):
    digits = {'0': 0, '1': 1, '2': 2, '=': -2, '-': -1 }
    if not number:
        return 0

    return 5 * from_snafu(number[:-1]) +  digits[number[-1]]


def part1(data):
    acc = 0
    for line in data:
        acc += from_snafu(line.rstrip())

    print(acc)
    return to_snafu(acc)


def main():
    print(part1(fileinput.input()))


if __name__ == '__main__':
    main()
