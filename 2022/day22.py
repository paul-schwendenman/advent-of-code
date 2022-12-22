import fileinput
from helper import *


def parse_input(data):
    hash = {}
    for line in data:
        name, operation = [part.strip() for part in line.split(':')]

        parts = operation.split(' ')

        if len(parts) == 1:
            hash[name] = int(parts[0])
        elif len(parts) == 3:
            hash[name] = parts

    return hash

def part1(data):
    pass


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
