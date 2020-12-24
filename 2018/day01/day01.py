from itertools import accumulate, cycle


def part1(frequencies):
    return sum(int(frequency) for frequency in frequencies)


def part2(raw_frequencies):
    frequencies = accumulate(cycle(int(f) for f in raw_frequencies))
    history = set()

    for frequency in frequencies:
        if frequency in history:
            break
        else:
            history.add(frequency)

    return frequency


def main():
    with open('input') as input_file:
        data = input_file.read().splitlines()
        print(part1(data))
        print(part2(data))


if __name__ == "__main__":
    main()
