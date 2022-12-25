import fileinput
from helper import *

def to_snafu(number):
    digits = {
        0: '0',
        1: '1',
        2: '2',
        3: '=',
        4: '-',
    }

    def inner(number):
        if number == 0:
            return tuple()
        remainder = number % 5
        rest = (number + 2) // 5

        return inner(rest) + (digits[remainder],)

    return ''.join(inner(number))


def from_snafu(digits):
    acc = 0
    for digit in digits:
        acc *= 5
        if digit == '1':
            acc += 1
        elif digit == '2':
            acc += 2
        elif digit == '3':
            acc += 3
        elif digit == '-':
            acc -= 1
        elif digit == '=':
            acc -= 2

    return acc


def part1(data):
    acc = 0
    for line in data:
        acc += from_snafu(line.rstrip())

    print(acc)
    return to_snafu(acc)


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
