import fileinput
import re
from collections import defaultdict


def part1(instructions):
    grid = defaultdict(bool)

    parser = re.compile(r'(?P<command>turn on|turn off|toggle) (?P<start_x>[0-9]+),(?P<start_y>[0-9]+) through (?P<end_x>[0-9]+),(?P<end_y>[0-9]+)')

    for instruction in instructions:
        match = parser.match(instruction).groupdict()
        command = match['command']
        start_x = int(match['start_x'])
        start_y = int(match['start_y'])
        end_x = int(match['end_x'])
        end_y = int(match['end_y'])

        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if command == 'turn on':
                    grid[(x, y)] = True
                elif command == 'turn off':
                    grid[(x, y)] = False
                elif command == 'toggle':
                    grid[(x, y)] = not grid[(x, y)]

    return sum(1 for x in range(0, 1000) for y in range(0, 1000) if grid[(x, y)])


def main():
    print(part1(fileinput.input()))


if __name__ == '__main__':
    main()