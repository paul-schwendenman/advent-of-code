import fileinput
from functools import lru_cache


@lru_cache(2000)
def triangular(n):
    return (n * (n + 1)) // 2


def part1(crabs):
    low = min(crabs)
    high = max(crabs)

    fuel = 1_000_000

    for i in range(low, high):
        new_fuel = sum(abs(crab - i) for crab in crabs)

        fuel = min(fuel, new_fuel)

    return fuel


def part2(crabs):
    low = min(crabs)
    high = max(crabs)

    fuel = 1_000_000_000_000

    for i in range(low, high+1):
        new_fuel = sum(triangular(abs(crab - i)) for crab in crabs)

        fuel = min(fuel, new_fuel)

    return fuel


def main():
    with fileinput.input() as input:
        positions = [int(value) for value in list(input)[0].split(",")]

    print(part1(positions))
    print(part2(positions))

    print(triangular.cache_info())


if __name__ == "__main__":
    main()
