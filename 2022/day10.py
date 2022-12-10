import fileinput


def part1(data):
	cycle = 1
	reg_x = 1
	strength = 0
	sample = [20, 60, 100, 140, 180, 220]

	for line in (l.rstrip() for l in data):
		if line == 'noop':
			cycle += 1

			if cycle in sample:
				print(f"@: {strength}\t += {reg_x} * {cycle} \t= {reg_x * cycle}")
				strength += reg_x * cycle
		else:
			value = int(line[4:])
			cycle += 1

			if cycle in sample:
				print(f"1: {strength}\t += {reg_x} * {cycle} \t= {reg_x * cycle}")
				strength += reg_x * cycle

			reg_x += value
			cycle += 1

			if cycle in sample:
				print(f"2: {strength}\t += {reg_x} * {cycle} \t= {reg_x * cycle}")
				strength += reg_x * cycle

	return strength


def get_sprite(cycle):
	yield (cycle - 1) % 40
	yield cycle % 40
	yield (cycle + 1) % 40

def part2(data):
	cycle = 0
	reg_x = 1
	crt = []

	for line in (l.rstrip() for l in data):
		if line == 'noop':
			cycle += 1

			if reg_x in get_sprite(cycle):
				crt.append('#')
			else:
				crt.append('.')
		else:
			value = int(line[4:])
			cycle += 1


			if reg_x in get_sprite(cycle):
				crt.append('#')
			else:
				crt.append('.')

			reg_x += value
			cycle += 1

			if reg_x in get_sprite(cycle):
				crt.append('#')
			else:
				crt.append('.')

	print_screen(crt)


def print_screen(crt):
	for row in (crt[0:40], crt[40:80], crt[80:120], crt[120:160], crt[160:200], crt[200:]):
		print(''.join(row))

def main():
	print(part1(fileinput.input()))
	# assert(part1(fileinput.input()) == 1912)
	print(part2(fileinput.input()))
	# assert(part2(fileinput.input()) == 2122)


if __name__ == '__main__':
	main()
