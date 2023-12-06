import fileinput
import re
import math
from tqdm import tqdm

def part1(data):
    times = map(int, re.findall(r'\d+', next(data)))
    distances = map(int, re.findall(r'\d+', next(data)))

    races = list(zip(times, distances))

    option_counts = []

    for max_time, goal in races:
        option_count = 0
        for wait_time in range(0, max_time):
            speed = wait_time
            distance = (max_time - wait_time) * speed

            if distance > goal:
                option_count += 1

        option_counts.append(option_count)

    return math.prod(option_counts)


def part2(data):
    max_time = int(''.join(re.findall(r'\d+', next(data))))
    record_distance = int(''.join(re.findall(r'\d+', next(data))))

    option_count = 0
    for wait_time in tqdm(range(0, max_time)):
        speed = wait_time
        distance = (max_time - wait_time) * speed

        if distance > record_distance:
            option_count += 1

    return option_count


def main():
    # print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
