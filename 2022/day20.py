import fileinput
from helper import *

class Wrapper:
    def __init__(self, number):
        self.number = number


def part1(data, decryption_key=1):

    sequence = tuple(extract_ints(line)[0] for line in data)
    working = deque(map(Wrapper, sequence))

    for item in tuple(working):
        item_index = working.index(item)

        working.rotate(-item_index)

        working.popleft()

        working.rotate(-item.number)

        working.appendleft(item)

    answer = [item.number for item in working]
    offset = answer.index(0)

    coords = [answer[(offset + n) % len(answer)] for n in (1000, 2000, 3000)]

    return sum(coords)


def part2(data, decryption_key=811589153):

    sequence = tuple(map(Wrapper, (extract_ints(line)[0] * decryption_key for line in data)))
    working = deque(sequence)


    for _ in range(10):
        for item in tuple(sequence):
            item_index = working.index(item)

            working.rotate(-item_index)

            working.popleft()

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
