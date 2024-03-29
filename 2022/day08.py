import fileinput


def part1(data):
	data = list(data)
	grid = {}
	visable = {}
	max_x = len(data[0].rstrip())
	max_y = len(data)

	for y, line in enumerate(data):
		for x, tree in enumerate(line.rstrip()):
			grid[(x,y)] = int(tree)

	for y in range(max_y):
		trees = [grid[(x, y)] for x in range(max_x)]

		max_tree = -1

		for x, tree in enumerate(trees):
			if tree > max_tree:
				visable[(x, y)] = True
				max_tree = tree

	for y in range(max_y):
		trees = [grid[(x, y)] for x in range(max_x - 1, -1, -1)]

		max_tree = -1

		for x_diff, tree in enumerate(trees):
			if tree > max_tree:
				visable[(max_x - x_diff - 1, y)] = True
				max_tree = tree

	for x in range(max_x):
		trees = [grid[(x, y)] for y in range(max_y - 1, -1, -1)]

		max_tree = -1

		for y_diff, tree in enumerate(trees):
			if tree > max_tree:
				visable[(x, max_y - y_diff - 1)] = True
				max_tree = tree

	for x in range(max_x):
		trees = [grid[(x, y)] for y in range(max_y)]

		max_tree = -1

		for y, tree in enumerate(trees):
			if tree > max_tree:
				visable[(x, y)] = True
				max_tree = tree

	return len(visable)


def directional_scenic_score(tree, neighboors, grid):
	count = 0

	for neighboor in neighboors:
		if tree > grid[neighboor]:
			count += 1
		elif tree <= grid[neighboor]:
			count += 1
			break
	return count

def part2(data):
	data = list(data)
	grid = {}
	score = {}
	max_x = len(data[0].rstrip())
	max_y = len(data)

	for y, line in enumerate(data):
		for x, tree in enumerate(line.rstrip()):
			grid[(x,y)] = int(tree)

	for y in range(max_y):
		for x in range(max_x):
			trees_above = [(x, y2) for y2 in range(y-1, -1, -1)]

			tas = directional_scenic_score(grid[(x, y)], trees_above, grid)

			trees_below = [(x, y2) for y2 in range(y+1, max_y)]
			tbs = directional_scenic_score(grid[(x, y)], trees_below, grid)

			trees_left = [(x2, y) for x2 in range(x-1, -1, -1)]
			tls = directional_scenic_score(grid[(x, y)], trees_left, grid)

			trees_right = [(x2, y) for x2 in range(x+1, max_x)]
			trs = directional_scenic_score(grid[(x, y)], trees_right, grid)

			score[(x, y)] = tas * tbs * tls * trs

	return max(score.values())


def main():
	print(part1(fileinput.input()))
	assert(part1(fileinput.input()) == 1776)
	print(part2(fileinput.input()))
	assert(part2(fileinput.input()) == 234416)


if __name__ == '__main__':
	main()
