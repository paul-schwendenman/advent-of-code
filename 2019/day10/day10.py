from collections import namedtuple, defaultdict
import math
from typing import Iterator, Sequence, DefaultDict


Point = namedtuple('Point', 'x y')


def calc_angle(point_1: Point, point_2: Point):
    dx = point_2.x - point_1.x
    dy = point_2.y - point_1.y
    return math.degrees(math.atan2(dx, -dy)) % 360


def calc_magnitude(point_1: Point, point_2: Point):
    dx = point_2.x - point_1.x
    dy = point_2.y - point_1.y

    return math.hypot(dx, dy)


def find_asteroids(grid) -> Iterator[Point]:
    for y_pos, row in enumerate(grid):
        for x_pos, asteroid in enumerate(row):
            if asteroid == '#':
                yield Point(x_pos, y_pos)


def calc_angles(focal_point: Point, asteroids: Sequence[Point]):
    return set(calc_angle(focal_point, asteroid) for asteroid in asteroids)


def group_by_angle(focal_point: Point, asteroids: Sequence[Point]):
    mapper: DefaultDict = defaultdict(list)

    for asteroid in asteroids:
        magnitude = calc_magnitude(focal_point, asteroid)
        angle = calc_angle(focal_point, asteroid)

        mapper[angle].append((magnitude, asteroid))

    return mapper


def combine_point(point: Point):
    return point.x * 100 + point.y


def part1(grid):
    asteroids = list(find_asteroids(grid))

    return max(len(calc_angles(asteroid, asteroids)) for asteroid in asteroids)


def part2(grid):
    asteroids = list(find_asteroids(grid))

    center = Point(13, 17)
    asteroids.remove(center)

    mapper = group_by_angle(center, asteroids)

    angles = sorted(calc_angles(center, asteroids))
    angle_200 = angles[199]

    winner = sorted(mapper[angle_200])[0][1]

    return combine_point(winner)


def main(filename="input"):
    with open(filename) as input_data:
        grid = input_data.read().splitlines()

    part1_solution = part1(grid)
    print(f'part 1 solution: {part1_solution}')
    part2_solution = part2(grid)
    print(f'part 2 solution: {part2_solution}')


if __name__ == "__main__":
    main()
