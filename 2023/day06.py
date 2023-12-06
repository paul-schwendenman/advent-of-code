import fileinput
import re
import itertools
import math
import functools
from tqdm import tqdm

def part1(data):
    times = map(int, re.findall(r'\d+', next(data)))
    distances = map(int, re.findall(r'\d+', next(data)))

    races = list(zip(times, distances))

    print(f'{races=}')
    option_counts = []

    for max_time, goal in races:
        option_count = 0
        for wait_time in range(0, max_time):
            speed = wait_time
            distance = (max_time - wait_time) * speed

            print(f'{wait_time=} {speed=} {distance=}')

            if distance > goal:
                option_count += 1

        option_counts.append(option_count)

    print(f'{option_counts=}')

    return math.prod(option_counts)


def part2(data):
    max_time = int(''.join(re.findall(r'\d+', next(data))))
    record_distance = int(''.join(re.findall(r'\d+', next(data))))


    # print(f'{record_distance=} {max_time=}')

    option_count = 0
    for wait_time in tqdm(range(0, max_time)):
        speed = wait_time
        distance = (max_time - wait_time) * speed

        # print(f'{wait_time=} {speed=} {distance=}')

        if distance > record_distance:
            option_count += 1


    # print(f'{option_count=}')

    return option_count
    pass

def main():
    # print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
