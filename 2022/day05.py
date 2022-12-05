import fileinput


def part1(data):
	instructions = list(data)[10:]

	stacks = {
		1: list("FDBZTJRN"),
		2: list("RSNJH"),
		3: list("CRNJGZFQ"),
		4: list('FVNGRTQ'),
		5: list('LTQF'),
		6: list('QCWZBRGN'),
		7: list('FCLSNHM'),
		8: list('DNQMTJ'),
		9: list('PGS'),
	}
	print(stacks)

	for instruction in instructions[:]:
		_, count, _, fromm, _, to = instruction.split(' ')

		print(instruction, count, fromm, to)
		for i in range(int(count)):
			stacks[int(to)].append(stacks[int(fromm)].pop())

	print(stacks)

	output = []

	for num, stack in sorted(stacks.items()):
		if len(stack):
			output += stack[len(stack) - 1]
		else:
			output += ' '

	return ''.join(output)


def part2(data):
	instructions = list(data)[10:]

	stacks = {
		1: list("FDBZTJRN"),
		2: list("RSNJH"),
		3: list("CRNJGZFQ"),
		4: list('FVNGRTQ'),
		5: list('LTQF'),
		6: list('QCWZBRGN'),
		7: list('FCLSNHM'),
		8: list('DNQMTJ'),
		9: list('PGS'),
	}
	print(stacks)

	for instruction in instructions[:]:
		_, count, _, fromm, _, to = instruction.split(' ')

		print(instruction, count, fromm, to)
		substack = []
		for i in range(int(count)):
			substack.append(stacks[int(fromm)].pop())

		stacks[int(to)].extend(reversed(substack))

	print(stacks)

	output = []

	for num, stack in sorted(stacks.items()):
		if len(stack):
			output += stack[len(stack) - 1]
		else:
			output += ' '

	return ''.join(output)
	pass


def main():
	print(part1(fileinput.input()))
	print(part2(fileinput.input()))


if __name__ == '__main__':
	main()
