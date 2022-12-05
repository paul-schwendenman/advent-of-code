import fileinput
import re
from collections import deque, namedtuple


Instruction = namedtuple('Instruction', 'count orig dest')


def parse_input(data):
	stack_labels = re.compile(r'( +[1-9]){1,9}')
	instrution_matcher = re.compile(r'move [0-9]+ from [1-9] to [1-9]')
	container_matcher = re.compile(r'((?:\[[A-Z]\])|(?: {3}) )+')

	label_line = None
	instructions = deque()
	stacks = {}

	for line in reversed(data):
		if stack_labels.match(line):
			label_line = line
			labels = line.split()
			for label in labels:
				stacks[label] = []
		elif instrution_matcher.match(line):
			_, count, _, orig, _, dest = line.split(' ')

			instructions.appendleft(Instruction(int(count), orig.rstrip(), dest.strip()))
		elif container_matcher.match(line):
			for stack_index in stacks.keys():
				try:
					value = line[label_line.index(stack_index)]
				except IndexError:
					value = ' '

				if value != ' ':
					stacks[stack_index].append(value)
			pass
		elif line.strip():
			raise ValueError('Parse error: %s', line)

	return instructions, stacks


def find_top(stacks):
	output = []

	for _, stack in sorted(stacks.items()):
		if len(stack):
			output += stack[len(stack) - 1]
		else:
			output += '?'

	return ''.join(output)


def part1(data):
	instructions, stacks = parse_input(list(data))

	for instruction in instructions:
		count, orig, dest = instruction

		for _ in range(count):
			stacks[dest].append(stacks[orig].pop())

	return find_top(stacks)


def part2(data):
	instructions, stacks = parse_input(list(data))

	for instruction in instructions:
		count, orig, dest = instruction

		substack = []
		for i in range(int(count)):
			substack.append(stacks[orig].pop())

		stacks[dest].extend(reversed(substack))

	return find_top(stacks)


def main():
	print(part1(fileinput.input()))
	# assert(part1(fileinput.input()) == 'QNNTGTPFN')
	print(part2(fileinput.input()))
	# assert(part2(fileinput.input()) == 'GGNPJBTTR')


if __name__ == '__main__':
	main()
