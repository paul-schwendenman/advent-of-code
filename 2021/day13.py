import fileinput

def print_paper(grid, max_y=6, max_x=39):
	for y in range(max_y):
		print("".join("█" if (x,y) in grid else " " for x in range(max_x)))

def part1(lines):
	dots = {}
	folds = []

	for line in lines:
		if 'fold' in line:
			folds.append(line)
		elif ',' in line:
			[x, y] = map(int, line.split(','))
			dots[(x,y)] = True

	for fold in folds[:1]:
		new_dots = {}
		direction = fold[11]
		value = int(fold[13:])

		if direction == 'y':
			for dot in dots.keys():
				x, y = dot
				if y > value:
					new_dots[(x,  value - (y - value))] = True
				elif y < value:
					new_dots[(x,  y)] = True

			pass
		elif direction == 'x':
			for dot in dots.keys():
				x, y = dot
				if x > value:
					new_dots[(value - (x - value), y)] = True
				elif x < value:
					new_dots[(x,  y)] = True
			pass
		dots = new_dots

	return len(dots)


def part2(lines):
	dots = {}
	folds = []

	for line in lines:
		if 'fold' in line:
			folds.append(line)
		elif ',' in line:
			[x, y] = map(int, line.split(','))
			dots[(x,y)] = True

	for fold in folds[:]:
		new_dots = {}
		direction = fold[11]
		value = int(fold[13:])

		if direction == 'y':
			for dot in dots.keys():
				x, y = dot
				if y > value:
					new_dots[(x,  value - (y - value))] = True
				elif y < value:
					new_dots[(x,  y)] = True

			pass
		elif direction == 'x':
			for dot in dots.keys():
				x, y = dot
				if x > value:
					new_dots[(value - (x - value), y)] = True
				elif x < value:
					new_dots[(x,  y)] = True
			pass
		dots = new_dots

	print_paper(dots)


def main():
	with fileinput.input() as input:
		lines = [line.strip() for line in input]

	print(part1(lines))
	print(part2(lines))

if __name__ == '__main__':
	main()