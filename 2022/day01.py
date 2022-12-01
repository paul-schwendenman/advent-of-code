import fileinput


def parse_snacks(data):
	return [[int(snack) for snack in elf.split('\n') if snack] for elf in ''.join(data).split('\n\n')]


def part1(data):
	max_seen = 0

	for elf_snacks in parse_snacks(data):
		total = sum(elf_snacks)

		if total > max_seen:
			max_seen = total

	return max_seen


def part2(data):
	elf_snack_totals =  sorted(map(lambda item: sum(item), parse_snacks(data)))

	return sum(elf_snack_totals[-3:])


def main():
	print(part1(fileinput.input()))
	print(part2(fileinput.input()))


if __name__ == '__main__':
	main()
