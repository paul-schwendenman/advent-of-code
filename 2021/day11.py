import fileinput
from collections import deque
from itertools import count


def print_grid(grid):
	for j in range(10):
		print("".join(str(grid[(i, j)]) for i in range(10)))


def parse_grid(grid):
	acc = {}

	for y, row in enumerate(grid):
		for x, item in enumerate(row):
			acc[(x, y)] = item

	return acc


def neighboors(x, y):
	for dy in [-1, 0, 1]:
		for dx in [-1, 0, 1]:
			if (dx, dy) != (0, 0):
				yield (x + dx, y + dy)



def simulate(grid):
	flashes = 0
	has_flashed = []

	for location in grid.keys():
		grid[location] += 1

	todo = deque(grid.keys())

	while len(todo) > 0:
		location = todo.popleft()

		brightness = grid[location]

		if brightness > 9 and location not in has_flashed:
			has_flashed.append(location)
			flashes += 1
			for neighboor in neighboors(*location):
				if neighboor in grid:
					grid[neighboor] += 1
					todo.append(neighboor)

	for location, brightness in grid.items():
		if brightness > 9:
			grid[location] = 0

	return grid, flashes



def part1(grid, steps=100):
	grid = parse_grid(grid)
	total_flashes = 0

	for i in range(steps):
		grid, flashes = simulate(grid)

		total_flashes += flashes

	return total_flashes


def part2(grid):
	grid = parse_grid(grid)

	for i in count(1):
		grid, flashes = simulate(grid)
		if flashes == 100:
			break

	return i


def main():
	with fileinput.input() as input:
		grid = [[int(item) for item in line.rstrip()] for line in input]

	print(part1(grid))
	print(part2(grid))

if __name__ == '__main__':
	main()