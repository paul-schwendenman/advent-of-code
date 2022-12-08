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

	for x in range(max_x):
		for y in range(max_y):
			if not (x, y) in visable:
				print(f"({x+1}, {y+1}): {grid[(x,y)]}")

	for y in range(max_y):
		for x in range(max_x):
			print('T' if not visable.get((x,y), False) else ' ', end='')
		print('')

	return len(visable)

	pass


def part2(data):
	pass


def main():
	print(part1(fileinput.input()))
	# assert(part1(fileinput.input()) == 1912)
	print(part2(fileinput.input()))
	# assert(part2(fileinput.input()) == 2122)


if __name__ == '__main__':
	main()
