import fileinput
import re
import math
from tqdm import tqdm


def sim_race_options(duration, record):
    options = 0

    for wait_time in tqdm(range(0, duration), leave=False):
        speed = wait_time
        go_time = duration - wait_time
        distance = go_time * speed

        if distance > record:
            options += 1

    return options


def part1(data):
    times = map(int, re.findall(r'\d+', next(data)))
    distances = map(int, re.findall(r'\d+', next(data)))

    races = list(zip(times, distances))

    option_counts = []

    for max_time, goal in races:
        option_count = sim_race_options(max_time, goal)

        option_counts.append(option_count)

    return math.prod(option_counts)


def part2(data):
    max_time = int(''.join(re.findall(r'\d+', next(data))))
    record_distance = int(''.join(re.findall(r'\d+', next(data))))

    option_count = sim_race_options(max_time, record_distance)

    return option_count


def main():
    data = list(fileinput.input())
    print(part1(iter(data)))
    print(part2(iter(data)))


if __name__ == '__main__':
    main()
