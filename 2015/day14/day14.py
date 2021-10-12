from enum import Enum
import fileinput
import re

class Stage(Enum):
	FLYING = 1
	RESTING = 0

class Reindeer():
	def __init__(self, name, speed, duration, rest):
		self.name = name
		self.speed = int(speed)
		self.duration = int(duration)
		self.rest = int(rest)

		self.location = 0
		self.stage = Stage.FLYING
		self.stage_duration = 0

	def step(self):
		if self.stage == Stage.FLYING:
			self.location += self.speed
			self.stage_duration += 1

			if self.stage_duration == self.duration:
				self.stage = Stage.RESTING
				self.stage_duration = 0
		else:
			self.stage_duration += 1

			if self.stage_duration == self.rest:
				self.stage = Stage.FLYING
				self.stage_duration = 0



def parse_reindeer(lines):
	pattern = re.compile(r"(?P<name>[A-Za-z]+) can fly (?P<speed>[0-9]+) km/s for (?P<duration>[0-9]+) seconds, but then must rest for (?P<rest>[0-9]+) seconds.")

	reindeer = []

	for line in lines:
		match = pattern.match(line)

		if match is None:
			raise ValueError("Bad line: %s", line)
		else:
			reindeer.append(Reindeer(match["name"], match["speed"], match["duration"], match["rest"]))

	return reindeer


def part1(lines, duration=1000):
	reindeer = parse_reindeer(lines)

	for _ in range(duration):
		for deer in reindeer:
			deer.step()

	return max(deer.location for deer in reindeer)



def main():
	print(part1(fileinput.input(), 2503))


if __name__ == "__main__":
	main()
