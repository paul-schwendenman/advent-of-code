import fileinput
from helper import *
from copy import copy

# class Wrapper(namedtuple())

def parse_all_ints(s):
    return list(map(int, s.split()))


def part1(data):
    # sequence = tuple(extract_ints(line)[0] for line in data)
    sequence = parse_all_ints(open('day20.in').read())
    working = deque(sequence)

    # print(sequence)

    for item in sequence:
        item_index = working.index(item)
        # start = working[0]
        # print(f'{item=} {item_index=}')
        # print(f'1. {working=}')

        # print(f'2. {working=} rotating {-item_index}')
        working.rotate(-item_index)

        # print(f'3. {working=} removing item')
        piece = working.popleft()

        # print(f'4. {working=} rotating {-piece}')
        working.rotate(-item)

        # print(f'5. {working=} adding {piece}')
        working.appendleft(item)
        # working.insert(0, item)

        # print(f'6. {working=} rotating {item_index+piece}={item_index}+{piece}')
        # working.rotate(item_index + piece)
        # print(f'6. {working=} rotating {item_index+piece}={item_index}+{piece}')
        # working.rotate(-working.index(start)+piece)


        # print(f'7. {working=}')
        # input()

    # print(f'F. {working=}')
    offset = working.index(0)
    # print(f'{offset=}')

    coords = [working[(offset + n) % len(sequence)] for n in (1000, 2000, 3000)]

    print(f'{coords=}')

    return sum(coords)
    pass


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
