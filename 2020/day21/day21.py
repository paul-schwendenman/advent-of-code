from __future__ import annotations
from typing import Sequence, Mapping, MutableMapping
from collections import defaultdict
from itertools import product
from functools import lru_cache, reduce
from aoc import readfile, tracer, profiler
import re


def parse_ingredients(line: str):
    ingredients, allergens = re.match(r'(.*) \(contains (.*)\)', line).groups()
    ingredients = set(ingredients.split(' '))
    allergens = set(allergens.split(', '))
    return ingredients, allergens


@profiler
def part1(data: Sequence[str]) -> int:
    labels = []
    ingredient_map = {}
    allergen_map: MutableMapping[str, set] = {}

    for line in data:
        labels.append(parse_ingredients(line))

    all_ingredients = reduce(set.union, [ingredients for ingredients, _ in labels])

    for ingredients, allergens in labels:
        # for ingredient in ingredients:
        #     pass
        for allergen in allergens:
            if allergen not in allergen_map:
                allergen_map[allergen] = ingredients
            else:
                allergen_map[allergen] = allergen_map[allergen].intersection(ingredients)

    print(allergen_map)
    all_possible_allergens = reduce(set.union, [ingredients for ingredients in allergen_map.values()])

    clean_ingredients = (all_ingredients - all_possible_allergens)
    print(clean_ingredients)

    return sum([len(ingredients.intersection(clean_ingredients)) for ingredients, _ in labels])



@profiler
def part2(data: Sequence[str]) -> str:
    labels = []
    allergen_map: MutableMapping[str, set] = {}

    for line in data:
        labels.append(parse_ingredients(line))

    all_ingredients = reduce(set.union, [ingredients for ingredients, _ in labels])

    for ingredients, allergens in labels:
        for allergen in allergens:
            if allergen not in allergen_map:
                allergen_map[allergen] = ingredients
            else:
                allergen_map[allergen] = allergen_map[allergen].intersection(ingredients)

    all_possible_allergens = reduce(set.union, [ingredients for ingredients in allergen_map.values()])

    clean_ingredients = (all_ingredients - all_possible_allergens)

    canonical = {}

    for allergen in allergen_map.keys():
        canonical[allergen] = (allergen_map[allergen] - clean_ingredients)

    used_ingredients = clean_ingredients.copy()

    while len(used_ingredients) < len(all_ingredients):
        for allergen, ingredients in canonical.items():
            remaining = ingredients - used_ingredients
            if len(remaining) == 1:
                canonical[allergen] = remaining
                used_ingredients = used_ingredients.union(remaining)

    return ','.join([canonical[allergen].pop() for allergen in sorted(allergen_map.keys())])


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
