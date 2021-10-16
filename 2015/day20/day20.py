from itertools import count


def part1(goal):

	for n in count():
		if n % 10000 == 0:
			print(n)
		if sum(i for i in range(1, n+1) if n % i == 0) * 10 > goal:
			break

	return n


def main():
	# print(part1(100))
	print(part1(36000000))


if __name__ == '__main__':
	main()