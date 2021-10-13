from dataclasses import dataclass
import fileinput
import re


@dataclass
class Ingredient():
	name: str
	capacity: int
	durability: int
	flavor: int
	texture: int
	calories: int

	def __post_init__(self):
		if not isinstance(self.capacity, int):
			self.capacity = int(self.capacity)
		if not isinstance(self.durability, int):
			self.durability = int(self.durability)
		if not isinstance(self.flavor, int):
			self.flavor = int(self.flavor)
		if not isinstance(self.texture, int):
			self.texture = int(self.texture)
		if not isinstance(self.calories, int):
			self.calories = int(self.calories)


def parse_ingredients(lines):
	pattern = re.compile(r'(?P<name>[A-Za-z]+): capacity (?P<capacity>-?[0-9]+), durability (?P<durability>-?[0-9]+), flavor (?P<flavor>-?[0-9]+), texture (?P<texture>-?[0-9]+), calories (?P<calories>-?[0-9]+)')
	ingredients = []


	for line in lines:
		match = pattern.match(line)

		if match is None:
			raise ValueError("Invalid line %s", line)
		else:
			ingredients.append(Ingredient(**match.groupdict()))

	return ingredients


def calc_score(ingredients: list[Ingredient], quanities):
	capacity = sum(quanity * ingredient.capacity for ingredient, quanity in zip(ingredients, quanities))
	durability = sum(quanity * ingredient.durability for ingredient, quanity in zip(ingredients, quanities))
	flavor = sum(quanity * ingredient.flavor for ingredient, quanity in zip(ingredients, quanities))
	texture = sum(quanity * ingredient.texture for ingredient, quanity in zip(ingredients, quanities))

	if any(value < 0 for value in (capacity, durability, flavor, texture)):
		return 0


	# print(capacity, durability, flavor, texture)
	return capacity * durability * flavor * texture

def part1(lines):
	ingredients = parse_ingredients(lines)

	print(ingredients)

	max_score = 0

	for first_quantity in range(101):
		for second_quanitity in range(100 - first_quantity):
			for third_quantity in range(100 - (first_quantity + second_quanitity)):
				fourth_quantity = 100 - (first_quantity + second_quanitity + third_quantity)

				quantities = [first_quantity, second_quanitity, third_quantity, fourth_quantity]

				score = calc_score(ingredients, quantities)

				if score > max_score:
					max_score = score
					# print(first_quantity, second_quanitity, third_quantity, fourth_quantity, score)
	return max_score


def main():
	print(part1(fileinput.input()))


if __name__ == '__main__':
	main()