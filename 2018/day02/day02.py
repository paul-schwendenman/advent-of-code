from collections import Counter
from itertools import combinations


def parse(box_id):
    counts = Counter(box_id).values()

    return (2 in counts, 3 in counts)


def difference(box_1, box_2):
    return sum(1 for pos_1, pos_2 in zip(box_1, box_2) if pos_1 != pos_2)


def common(box_1, box_2):
    return ''.join(char
                   for index, char in enumerate(box_1)
                   if char == box_2[index])


def part1(box_ids):
    twos = 0
    threes = 0

    for box_id in box_ids:
        two, three = parse(box_id)

        if two:
            twos += 1
        if three:
            threes += 1

    return threes * twos


def part2(box_ids):
    for box_1, box_2 in combinations(box_ids, 2):
        if difference(box_1, box_2) == 1:
            break
    else:
        raise ValueError("Pairing not found")

    return common(box_1, box_2)


def main():
    with open('input') as input_file:
        data = input_file.read().splitlines()
        print(part1(data))
        print(part2(data))


if __name__ == "__main__":
    main()
