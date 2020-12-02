from collections import Counter
import fileinput
import re


def parse_line(line):
    return re.match(r'(?P<min>[0-9]+)-(?P<max>[0-9]+) (?P<char>.): (?P<password>.+)', line).groups()


def part1(lines):
    count = 0
    for line in lines:
        min, max, char, password = parse_line(line)

        c = Counter(password)

        if c[char] >= int(min) and c[char] <= int(max):
            count += 1

    return count


def part2(lines):
    count = 0
    for line in lines:
        min, max, char, password = parse_line(line)

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
