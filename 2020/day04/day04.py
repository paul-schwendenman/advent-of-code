from contextlib import contextmanager
import fileinput


@contextmanager
def readfile(filename=None):
    with fileinput.input(filename) as data:
        yield [line.rstrip() for line in data]


def part1(data):
    pass


def part2(data):
    pass


def main():
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
