from collections import namedtuple
from dataclasses import dataclass
from typing import Optional
from itertools import product, combinations
from copy import copy

@dataclass
class Item:
	cost: int
	damage: int
	armor: int


@dataclass
class Player:
	hit_points: int
	damage: int
	armor: int
	gold: int = 0

	def add_item(self, item: Optional[Item]):
		if not item:
			return

		self.damage += item.damage
		self.gold += item.cost
		self.armor += item.armor

	def take_hit(self, damage: int) -> None:
		self.hit_points -= max(1, damage - self.armor)

	def is_dead(self) -> bool:
		return self.hit_points <= 0


# Weapons:    Cost  Damage  Armor
# Dagger        8     4       0
# Shortsword   10     5       0
# Warhammer    25     6       0
# Longsword    40     7       0
# Greataxe     74     8       0
weapons = [
	Item(8, 4, 0),
	Item(10, 5, 0),
	Item(25, 6, 0),
	Item(40, 7, 0),
	Item(74, 8, 0),
]

# Armor:      Cost  Damage  Armor
# Leather      13     0       1
# Chainmail    31     0       2
# Splintmail   53     0       3
# Bandedmail   75     0       4
# Platemail   102     0       5
armors = [
	Item(13, 0, 1),
	Item(31, 0, 2),
	Item(53, 0, 3),
	Item(75, 0, 4),
	Item(102, 0, 5),
	None,
]

# Rings:      Cost  Damage  Armor
# Damage +1    25     1       0
# Damage +2    50     2       0
# Damage +3   100     3       0
# Defense +1   20     0       1
# Defense +2   40     0       2
# Defense +3   80     0       3
rings = [
	Item(25, 1, 0),
	Item(50, 2, 0),
	Item(100, 3, 0),
	Item(20, 0, 1),
	Item(40, 0, 2),
	Item(80, 0, 3),
	None,
	None,
]

def simulate(you: Player, boss: Player) -> bool:
	while True:
		boss.take_hit(you.damage)

		if boss.is_dead():
			return True

		you.take_hit(boss.damage)

		if you.is_dead():
			return False

def part1(boss):
	ring_choices = combinations(rings, 2)
	costs = []

	for (weapon, armor, (ring1, ring2)) in product(weapons, armors, ring_choices):
		you = Player(100, 0, 0)
		you.add_item(weapon)
		you.add_item(armor)
		you.add_item(ring1)
		you.add_item(ring2)

		if simulate(you, copy(boss)):
			costs.append(you.gold)

	return min(costs)


def part2(boss):
	ring_choices = combinations(rings, 2)
	costs = []

	for (weapon, armor, (ring1, ring2)) in product(weapons, armors, ring_choices):
		you = Player(100, 0, 0)
		you.add_item(weapon)
		you.add_item(armor)
		you.add_item(ring1)
		you.add_item(ring2)

		if not simulate(copy(you), copy(boss)):
			costs.append(you.gold)

	return max(costs)


def example():
	you = Player(8, 5, 5)
	boss = Player(12, 7, 2)

	return simulate(you, boss)


def main():
	boss = Player(100, 8, 2)
	print(part1(boss))
	print(part2(boss))

if __name__ == "__main__":
	main()
