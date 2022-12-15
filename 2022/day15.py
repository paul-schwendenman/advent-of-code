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

    def uncovered_spaces(self):
        sx, sy, md = self.sensor.x, self.sensor.y, self.manhattan_distance + 1


        for x in range(sx-md, sx+md+1):
            ty = sy - (md - abs(sx - x))
            by = sy + (md - abs(sx - x))

            assert self.distance_from(Point(x, ty)) - 1 == self.manhattan_distance
            assert self.distance_from(Point(x, by)) - 1 == self.manhattan_distance

            yield Point(x, ty)
            yield Point(x, by)




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
        # for point in sensor.covered_spaces(goal_y):
        for point in sensor.covered_spaces2(0, 21):
            grid[point.y][point.x] = 'X'

    for y in range(0, 21):
        print(''.join('X' if x in grid[y] else '.' for x in range(0, 21)))

    return len(grid[goal_y])


def part2_old(data, min_coord=0, max_coord=4000000):
    grid = defaultdict(dict)

    sensors = parse_input(data)

    for index, sensor in enumerate(sensors, start=1):
        print(f'---- Sensor {index} ----')
        for point in sensor.covered_spaces2(min_coord, max_coord):
            grid[point.y][point.x] = 'X'

    for y in range(0, 21):
        print(''.join('X' if x in grid[y] else '.' for x in range(0, 21)))

    for y, row in grid.items():
        if len(row) < max_coord:
            for x in range(min_coord, max_coord + 1):
                if x not in row:
                    print(x, y)
                    return x * 4_000_000 + y


def part2(data, min_coord=0, max_coord=4000000):
    grid = defaultdict(dict)

    sensors = list(parse_input(data))

    spaces = set()

    for sensor in sensors:
        spaces = spaces.union(sensor.uncovered_spaces())

    for index, space in enumerate(spaces, start=1):
        if index % (len(spaces) // 100) == 0:
            print(f'------ {index} -------')
        if not (min_coord <= space.x <= max_coord) or not (min_coord <= space.y <= max_coord):
            continue
        if all(not sensor.can_detect(space) for sensor in sensors):
            print(space)
            return space.x * 4_000_000 + space.y




def main():
    # print(part1(fileinput.input(), 10))
    # print(part1(fileinput.input()))
    # print(part2(fileinput.input(), 0, 20))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
