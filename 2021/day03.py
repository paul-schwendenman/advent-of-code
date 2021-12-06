import fileinput
from collections import Counter


def transpose(grid):
    return list(zip(*grid))


def part1(rows):
    gamma_list = []
    epsilon_list = []

    columns = transpose(rows)

    for column in columns:
        c = Counter(column)

        gamma_list.append(c.most_common()[0][0])
        epsilon_list.append(c.most_common()[1][0])

    gamma = int(''.join(gamma_list), 2)
    epsilon = int(''.join(epsilon_list), 2)

    return gamma * epsilon


def calc_fancy_rating(rows, func):
    guesses = rows
    for i in (range(len(rows[0]))):
        c = Counter(item[i] for item in guesses)

        guesses = list(filter(lambda item: item[i] == func(c), guesses))
        if len(guesses) == 1:
            break
    else:
        raise ValueError("Did not find one scrub value")

    return int(guesses[0], 2)


def calc_co2_scrubber_rating(rows):
    return calc_fancy_rating(rows, lambda c: '1' if c['0'] > c['1'] else '0')


def calc_oxygen_generator_rating(rows):
    return calc_fancy_rating(rows, lambda c: '0' if c['0'] > c['1'] else '1')


def part2(rows):
    oxygen_generator_rating, CO2_scrubber_rating = calc_oxygen_generator_rating(rows), calc_co2_scrubber_rating(rows)

    return oxygen_generator_rating * CO2_scrubber_rating


def main():
    with fileinput.input() as raw_data:
        data = [line.rstrip() for line in raw_data]

    print(part1(data))
    print(part2(data))


if __name__ == '__main__':
    main()
