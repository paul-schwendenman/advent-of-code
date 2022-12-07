import fileinput
import os.path
from collections import defaultdict
from dataclasses import dataclass

class Directory:
	def __init__(self, name, parent=None):
		self.name = name
		self.parent = parent

		self.children = []

	def add_child(self, child):
		self.children.append(child)

	def path(self):
		if self.parent:
			return self.parent.path()[:] + [self.name]
		else:
			return ['/']

	@property
	def size(self):
		return sum(child.size for child in self.children)



@dataclass
class File:
	name: str
	size: int



def part1(data):
	current = None
	dirs = []

	for line in [l.strip() for l in data]:
		print(line)
		if line[:4] == '$ cd':
			if line == '$ cd ..':
				current = current.parent
			else:
				name = line.split(' ')[-1]

				dir = Directory(name, current)
				dirs.append(dir)
				if current:
					current.add_child(dir)

				current = dir
			print(current.path())
		elif line == '$ ls':
			pass
		elif line[:4] == 'dir ':

			pass
		else:
			size, name = line.split(' ')

			file = File(name, int(size))
			current.add_child(file)


	print([(dir.name, dir.size) for dir in dirs if dir.size < 100000])
	return sum(dir.size for dir in dirs if dir.size < 100000)
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
