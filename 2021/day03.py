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


def part2(rows):
    columns = transpose(rows)

    oxygen_guesses = rows
    scrub_guesses = rows

    for i in (range(len(columns))):
        c = Counter(item[i] for item in oxygen_guesses)

        filter_on = '0' if c['0'] > c['1'] else '1'

        oxygen_guesses = list(filter(lambda item: item[i] == filter_on, oxygen_guesses))
        if len(oxygen_guesses) == 1:
            break

    for i in (range(len(columns))):
        c = Counter(item[i] for item in scrub_guesses)
        if c['1'] < c['0']:
            filter_on = '1'
        else:
            filter_on = '0'
        scrub_guesses = list(filter(lambda item: item[i] == filter_on, scrub_guesses))
        if len(scrub_guesses) == 1:
            break
    else:
        raise ValueError("Did not find one scrub value")

    oxygen_generator_rating, CO2_scrubber_rating = int(oxygen_guesses[0], 2), int(scrub_guesses[0], 2)

    return oxygen_generator_rating * CO2_scrubber_rating

def main():
    with fileinput.input() as raw_data:
        data = [line.rstrip() for line in raw_data]

    print(part1(data))
    print(part2(data))

if __name__ == '__main__':
    main()
