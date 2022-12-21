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

    @lru_cache
    def solve(start):
        value = hash[start]
        if start == 'humn':
            return 'X'
        elif isinstance(value, int):
            return value
        elif start == 'root':
            return f'({solve(value[0])} = {solve(value[2])})'
        if isinstance(solve(value[0]), int) and isinstance(solve(value[2]), int):
            if value[1] == '+':
                return solve(value[0]) + solve(value[2])
            elif value[1] == '-':
                return solve(value[0]) - solve(value[2])
            elif value[1] == '*':
                return solve(value[0]) * solve(value[2])
            elif value[1] == '/':
                return int(solve(value[0]) / solve(value[2]))

        elif value[1] == '+':
            return f'({solve(value[0])} + {solve(value[2])})'
        elif value[1] == '-':
            return f'({solve(value[0])} - {solve(value[2])})'
        elif value[1] == '*':
            return f'({solve(value[0])} * {solve(value[2])})'
        elif value[1] == '/':
            return f'({solve(value[0])} / {solve(value[2])})'
        else:
            raise ValueError(f"{start} {hash[start]}")

    return solve('root')
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
