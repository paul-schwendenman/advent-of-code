import fileinput
from helper import extract_ints
from collections import namedtuple, defaultdict
from dataclasses import dataclass


class Point(namedtuple('Point', 'x y')):
    __slots__ = ()


def calc_manhatten_distance(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

@dataclass
class Sensor:
    sensor: Point
    beacon: Point

    @property
    def manhattan_distance(self):
        return calc_manhatten_distance(self.beacon, self.sensor)

    def distance_from(self, point):
        return calc_manhatten_distance(self.sensor, point)

    def can_detect(self, point):
        return self.distance_from(point) <= self.manhattan_distance

    def covered_spaces(self, goal_y):
        max_x = self.sensor.x + self.manhattan_distance + 1
        min_x = self.sensor.x - self.manhattan_distance
        max_y = self.sensor.y + self.manhattan_distance + 1
        min_y = self.sensor.y - self.manhattan_distance

        if not (min_y <= goal_y <= max_y):
            yield from []

        for x in range(min_x, max_x):
            # for y in range(min_y, max_y):
                point = Point(x, goal_y)
                if point == self.beacon or point == self.sensor:
                    continue
                if self.distance_from(point) <= self.manhattan_distance:
                    yield point

    def covered_spaces2(self, min_coord, max_coord):
        max_x = min(self.sensor.x + self.manhattan_distance + 1, max_coord)
        min_x = max(self.sensor.x - self.manhattan_distance, min_coord)
        max_y = min(self.sensor.y + self.manhattan_distance + 1, max_coord)
        min_y = max(self.sensor.y - self.manhattan_distance, min_coord)

        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                point = Point(x, y)
                # if point == self.beacon or point == self.sensor:
                    # continue
                if self.distance_from(point) <= self.manhattan_distance:
                    yield point



def parse_line(line):
    sx, sy, bx, by = extract_ints(line)

    return Sensor(Point(sx, sy), Point(bx, by))

def parse_input(data):
    return (parse_line(line) for line in data)


def part1(data, goal_y=2_000_000):
    grid = defaultdict(dict)

    sensors = parse_input(data)

    for index, sensor in enumerate(sensors, start=1):
        print(f'---- Sensor {index} ----')
        for point in sensor.covered_spaces(goal_y):
            grid[point.y][point.x] = 'X'

    print(''.join('X' if x in grid[9] else '.' for x in range(-5, 30)))
    print(''.join('X' if x in grid[10] else '.' for x in range(-5, 30)))
    print(''.join('X' if x in grid[11] else '.' for x in range(-5, 30)))

    return len(grid[goal_y])


def part2(data, min_coord=0, max_coord=4000000):
    grid = defaultdict(dict)

    sensors = parse_input(data)

    for index, sensor in enumerate(sensors, start=1):
        print(f'---- Sensor {index} ----')
        for point in sensor.covered_spaces2(min_coord, max_coord):
            grid[point.y][point.x] = 'X'

    print(''.join('X' if x in grid[9] else '.' for x in range(-5, 30)))
    print(''.join('X' if x in grid[10] else '.' for x in range(-5, 30)))
    print(''.join('X' if x in grid[11] else '.' for x in range(-5, 30)))

    for y, row in grid.items():
        if len(row) < max_coord:
            for x in range(min_coord, max_coord + 1):
                if x not in row:
                    print(x, y)
                    return x * 4_000_000 + y

    pass


def main():
    # print(part1(fileinput.input(), 10))
    # print(part1(fileinput.input()))
    # print(part2(fileinput.input(), 0, 20))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
