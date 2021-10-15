from enum import Enum
from collections import namedtuple, defaultdict
import fileinput


class Point(namedtuple('Point', 'x y')):
    __slots__ = ()

    def get_neighboors(self):
        for offset in ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1)):
            yield self + offset

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])


class Light(Enum):
	ON = "#"
	OFF = "."


def make_grid(lines):
	grid = {}

	for y, line in enumerate(lines):
		for x, light in enumerate(line.rstrip()):
			grid[Point(x, y)] = Light(light)

	return grid, y

def print_grid(grid, length = 100):
	for y in range(length):
		print("".join("#" if grid.get(Point(x, y)) == Light.ON else '.' for x in range(length)))

	print()


def step(grid):
	new_grid = {}

	for point, light in grid.items():
		count = sum(1 for neighboor in point.get_neighboors() if grid.get(neighboor, Light.OFF) == Light.ON )
		if light == Light.ON:
			if count in (2, 3):
				new_grid[point] = Light.ON
			else:
				new_grid[point] = Light.OFF
		if light == Light.OFF:
			if count == 3:
				new_grid[point] = Light.ON
			else:
				new_grid[point] = Light.OFF

	return new_grid


def count_lights(grid):
	return sum(1 for light in grid.values() if light == Light.ON)


def part1(lines, steps):
	grid, _ = make_grid(lines)
	# print_grid(grid, 6)

	for _ in range(steps):
		grid = step(grid)
		# print_grid(grid, 6)

	return count_lights(grid)

def part2(lines, steps):
	grid, side = make_grid(lines)
	# print_grid(grid, 6)

	for _ in range(steps):
		grid = step(grid)
		grid[Point(0, 0)] = Light.ON
		grid[Point(side, 0)] = Light.ON
		grid[Point(0, side)] = Light.ON
		grid[Point(side, side)] = Light.ON
		# print_grid(grid, 6)

	return count_lights(grid)


def main():
	# print(part1(fileinput.input(), 4))
	print(part1(fileinput.input(), 100))
	# print(part2(fileinput.input(), 5))
	print(part2(fileinput.input(), 100))


if __name__ == '__main__':
	main()