from __future__ import annotations
from typing import List, Sequence, Mapping, MutableMapping, Tuple
from functools import reduce
from aoc import readfile, profiler
import re


def parse_ingredients(line: str) -> Tuple[set, set]:
    match = re.match(r'(.*) \(contains (.*)\)', line)

    if match:
        raw_ingredients, raw_allergens = match.groups()
    else:
        raise ValueError("Invalid line:", line)

    ingredients = set(raw_ingredients.split(' '))
    allergens = set(raw_allergens.split(', '))
    return ingredients, allergens


def generate_allergen_map(labels: List[Tuple[set, set]]) -> Mapping[str, set]:
    allergen_map: MutableMapping[str, set] = {}
    for ingredients, allergens in labels:
        for allergen in allergens:
            if allergen not in allergen_map:
                allergen_map[allergen] = ingredients
            else:
                allergen_map[allergen] = allergen_map[allergen].intersection(ingredients)
    return allergen_map


@profiler
def part1(data: Sequence[str]) -> int:
    labels = [parse_ingredients(line) for line in data]
    allergen_map = generate_allergen_map(labels)

    all_ingredients = reduce(set.union, [ingredients for ingredients, _ in labels])

    all_possible_allergens = reduce(set.union, [ingredients for ingredients in allergen_map.values()])

    clean_ingredients = (all_ingredients - all_possible_allergens)

    return sum([len(ingredients.intersection(clean_ingredients)) for ingredients, _ in labels])


@profiler
def part2(data: Sequence[str]) -> str:
    labels = [parse_ingredients(line) for line in data]
    allergen_map = generate_allergen_map(labels)

    all_ingredients = reduce(set.union, [ingredients for ingredients, _ in labels])

    all_possible_allergens = reduce(set.union, [ingredients for ingredients in allergen_map.values()])

    used_ingredients = (all_ingredients - all_possible_allergens)

    final = {}

    while all_ingredients - used_ingredients:
        for allergen, ingredients in allergen_map.items():
            remaining = ingredients - used_ingredients
            if len(remaining) == 1:
                used_ingredients = used_ingredients.union(remaining)
                final[allergen] = remaining.pop()

    return ','.join([final[allergen] for allergen in sorted(allergen_map.keys())])


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
