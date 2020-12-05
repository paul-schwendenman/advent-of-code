from contextlib import contextmanager
import fileinput


@contextmanager
def readfile(filename=None):
    with fileinput.input(filename) as data:
        yield [line.rstrip() for line in data]

def decode(row):
    # print(row)
    seat = list(map(lambda a: '1' if a == 'B' or a == 'R' else '0', row))
    # print(seat)
    return int(''.join(seat), base=2)

def seat(boarding_pass):
    row, column = boarding_pass[:7], boarding_pass[7:]
    # print(row, column)
    row = decode(row)
    column = decode(column)
    seat = row*8 + column
    # print(row, ' ', column, ' ', seat)
    return seat


def part1(data):
    return max([seat(boarding_pass) for boarding_pass in data])


def part2(data):
    passes = ([seat(boarding_pass) for boarding_pass in data])
    for i in range(1024):
        if i not in passes:
            print (i)



def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
