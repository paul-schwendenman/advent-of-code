import fileinput
from itertools import count

def fire(dx, dy, x_min, x_max, y_min, y_max):
	highest_point = -1_000_000_000
	x, y = (0, 0)

	while x < x_max and y > y_min:
		x += dx
		y += dy

		dx += -1 if dx > 0 else -1 if dx < 0 else 0
		dy -= 1

		# print(x,y)

		if highest_point < y:
			highest_point = y

		if x_min <= x <= x_max and y_min <= y <= y_max:
			# print('hit')
			return True, highest_point
		# else:
			# print('miss')

	return False, None

def part1(data):
	target_area = data[0][13:].split(', ')
	highest_point = -1_000_000_000

	[x_min, x_max] = [int(item) for item in target_area[0][2:].split('..')]
	[y_min, y_max] = [int(item) for item in target_area[1][2:].split('..')]

	print(x_min, x_max)
	print(y_min, y_max)

	x, y = (0, 0)

	velocity = 6, 9
	dx, dy = velocity
	target_velocity = None


	for dy in range(-1000, 1000):
		for dx in range(100):
	# for dx in count(1):
	# 	for dy in count(-1000):
			hit, new_highest_point = fire(dx, dy, x_min, x_max, y_min, y_max)

			if hit and new_highest_point > highest_point:
				highest_point = new_highest_point
				target_velocity = dx, dy

	print(f'target velocity: {target_velocity}')
	print(f'highest point: {highest_point}')

	return highest_point


def part2(data):
	target_area = data[0][13:].split(', ')
	highest_point = -1_000_000_000
	velocities = []

	[x_min, x_max] = [int(item) for item in target_area[0][2:].split('..')]
	[y_min, y_max] = [int(item) for item in target_area[1][2:].split('..')]

	print(x_min, x_max)
	print(y_min, y_max)

	x, y = (0, 0)

	velocity = 6, 9
	dx, dy = velocity
	target_velocity = None


	for dy in range(-1000, 3000):
		for dx in range(1000):
	# for dx in count(1):
	# 	for dy in count(-1000):
			hit, new_highest_point = fire(dx, dy, x_min, x_max, y_min, y_max)

			if hit:
				highest_point = new_highest_point
				target_velocity = dx, dy
				velocities.append((dx, dy))

	print(f'target velocity: {target_velocity}')
	print(f'highest point: {highest_point}')

	print(velocities)

	return len(velocities)
	pass


def main():
    with fileinput.input() as input:
        data = [line.rstrip() for line in input]

    # print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
