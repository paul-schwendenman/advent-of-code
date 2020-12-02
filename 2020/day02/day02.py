from collections import Counter
import fileinput
import re

def parse_line(line):
    return re.match(r'([0-9]+)-([0-9]+) (.): (.+)', line).groups()


def part1(lines):
    count = 0
    for line in lines:
        print(line)
        min, max, char, password = parse_line(line)
        print(min, max, char, password)

        c = Counter(password)
        print(c)

        if c[char] >= int(min) and c[char] <= int(max):
            count += 1

    return count


def part2(lines):
    count = 0
    for line in lines:
        print(line)
        min, max, char, password = parse_line(line)
        print(min, max, char, password)

        if (password[int(min)-1] == char and password[int(max)-1] != char) or (password[int(min)-1] != char and password[int(max)-1] == char):
            count += 1

    return count


def main():
    with fileinput.input() as data:
        lines = [line for line in data]

    print(part1(lines))
    print(part2(lines))


if __name__ == '__main__':
    main()
