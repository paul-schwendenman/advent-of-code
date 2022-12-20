import fileinput
from helper import *

# @dataclass
class Wrapper:
    def __init__(self, number):
        self.number = number
    # number: int

def parse_all_ints(s):
    return list(map(int, s.split()))


def part1(data, decryption_key=1):

    sequence = tuple(extract_ints(line)[0] for line in data)
    working = deque(map(Wrapper, sequence))

    # print(sequence)

    for item in tuple(working):
        item_index = working.index(item)
        # start = working[0]
        # print(f'{item=} {item_index=}')
        # print(f'1. {working=}')

        # print(f'2. {working=} rotating {-item_index}')
        working.rotate(-item_index)

        # print(f'3. {working=} removing item')
        piece = working.popleft()

        # print(f'4. {working=} rotating {-piece}')
        working.rotate(-item.number)

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
    answer = [item.number for item in working]
    offset = answer.index(0)
    # print(f'{offset=}')

    coords = [answer[(offset + n) % len(answer)] for n in (1000, 2000, 3000)]

    return sum(coords)


def part2(data, decryption_key=811589153):

    sequence = tuple(map(Wrapper, (extract_ints(line)[0] * decryption_key for line in data)))
    working = deque(sequence)


    for _ in range(10):
        for item in tuple(sequence):
            item_index = working.index(item)

            working.rotate(-item_index)

            piece = working.popleft()

            working.rotate(-item.number)

            working.appendleft(item)

    answer = [item.number for item in working]
    offset = answer.index(0)

    coords = [answer[(offset + n) % len(answer)] for n in (1000, 2000, 3000)]

    return sum(coords)


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
