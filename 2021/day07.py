import fileinput


def part1(positions):
    low = min(positions)
    high = max(positions)

    fuel = 1_000_000
    location = None

    for i in range(low, high+1):
        new_fuel = sum(abs(crab - i) for crab in positions)

        if new_fuel < fuel:
            # print(f'swapping: {new_fuel} fuel to {i}')

            fuel = new_fuel
            location = i
    return fuel

def part2(positions):
    low = min(positions)
    high = max(positions)

    fuel = 1_000_000_000_000
    location = None

    triangular = lambda n: (n * (n + 1)) // 2

    for i in range(low, high+1):
        new_fuel = sum(triangular(abs(crab - i)) for crab in positions)

        if new_fuel < fuel:
            # print(f'swapping: {new_fuel} fuel to {i}')

            fuel = new_fuel
            location = i
    return fuel
    pass


def main():
    with fileinput.input() as input:
        positions = [int(value) for value in list(input)[0].split(",")]

    print(part1(positions))
    print(part2(positions))


if __name__ == "__main__":
    main()
