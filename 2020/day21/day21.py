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
    print(ingredients)
    print(allergens)
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
        print("loop:", allergens, ingredients)
        for allergen in allergens:
            print("a:", allergen)
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
def part2(data: Sequence[str]) -> int:
    pass


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
