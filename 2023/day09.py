import fileinput
import itertools


def parse_input(data):
    for line in data:
        yield [int(item) for item in line.split(' ')]


def extend_sequence(sequence):
    if all(map(lambda item: item == 0, sequence)):
        # print(f'{[0] + seq[:] + [0]}')
        return [0, 0]

    [first_diff, *_, last_diff] = extend_sequence([b - a for a, b in itertools.pairwise(sequence)])

    # print(f'{[seq[0] - differences[0]] + seq[:] + [seq[-1] + differences[-1]]}')
    return [sequence[0] - first_diff, sequence[-1] + last_diff]


def part1(data):
    return sum(extend_sequence(sequence)[-1] for sequence in parse_input(data))


def part2(data):
    return sum(extend_sequence(sequence)[0] for sequence in parse_input(data))


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
