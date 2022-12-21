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
    hash = parse_input(data)

    def solve(start):
        value = hash[start]
        if isinstance(value, int):
            return value
        elif value[1] == '+':
            return solve(value[0]) + solve(value[2])
        elif value[1] == '-':
            return solve(value[0]) - solve(value[2])
        elif value[1] == '*':
            return solve(value[0]) * solve(value[2])
        elif value[1] == '/':
            return solve(value[0]) / solve(value[2])
        else:
            raise ValueError(f"{start} {hash[start]}")

    return int(solve('root'))


def part2(data):
    hash = parse_input(data)

    def solve(start, human=None):
        value = hash[start]
        if start == 'humn':
            return human
        elif isinstance(value, int):
            return value
        elif start == 'root':
            raise ValueError('Found root')
        if value[1] == '+':
            return solve(value[0], human) + solve(value[2], human)
        elif value[1] == '-':
            return solve(value[0], human) - solve(value[2], human)
        elif value[1] == '*':
            return solve(value[0], human) * solve(value[2], human)
        elif value[1] == '/':
            return int(solve(value[0], human) / solve(value[2], human))
        else:
            raise ValueError(f"{start} {hash[start]}")

    left = hash['root'][0]
    right = hash['root'][2]

    target = solve(right)

    lower_bound = 0
    upper_bound = int(1e20)

    while lower_bound < upper_bound:
        middle = (lower_bound + upper_bound) // 2
        diff = solve(left, middle) - target
        if diff == 0:
            return middle
        elif diff > 0:
            lower_bound = middle
        else:
            upper_bound = middle

    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
