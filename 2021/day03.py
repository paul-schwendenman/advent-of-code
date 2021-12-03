import fileinput
from collections import Counter



def part1():
    gamma_list = []
    epsilon_list = []
    with fileinput.input() as data:

        lines = list(zip(*(l.rstrip() for l in data)))

        for column in lines:
            c = Counter(column)
            c.most_common

            gamma_list.append(c.most_common()[0][0])
            epsilon_list.append(c.most_common()[1][0])

    gamma, epsilon = int(''.join(gamma_list), 2), int(''.join(epsilon_list), 2)

    print(gamma, epsilon)
    return gamma * epsilon

def part2():
    gamma_list = []
    epsilon_list = []
    with fileinput.input() as raw_data:
        data = list(raw_data)


    lines = list(zip(*(l.rstrip() for l in data)))

    for column in lines:
        c = Counter(column)
        c.most_common

        gamma_list.append(c.most_common()[0][0])
        epsilon_list.append(c.most_common()[1][0])

    gamma, epsilon = int(''.join(gamma_list), 2), int(''.join(epsilon_list), 2)

    oxigen_guesses = data
    scrub_guesses = data

    for i in (range(len(lines))):
        c = Counter(item[i] for item in oxigen_guesses)
        if c['0'] > c['1']:
            filter_on = '0'
        else:
            filter_on = '1'
        oxigen_guesses = list(filter(lambda item: item[i] == filter_on, oxigen_guesses))
        print(oxigen_guesses, gamma_list[i], i)
        if len(oxigen_guesses) == 1:
            break
    for i in (range(len(lines))):
        c = Counter(item[i] for item in scrub_guesses)
        if c['1'] < c['0']:
            filter_on = '1'
        else:
            filter_on = '0'
        scrub_guesses = list(filter(lambda item: item[i] == filter_on, scrub_guesses))
        if len(scrub_guesses) == 1:
            break
    else:
        print("fail")

    print( oxigen_guesses, scrub_guesses)

    oxygen_generator_rating, CO2_scrubber_rating = int(oxigen_guesses[0], 2), int(scrub_guesses[0], 2)

    print(oxygen_generator_rating, CO2_scrubber_rating)
    return oxygen_generator_rating * CO2_scrubber_rating

def main():
    print(part1())
    print(part2())

if __name__ == '__main__':
    main()
