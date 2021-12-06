import fileinput
from collections import Counter


def solve(fish, days=80):
    fish = dict(Counter(fish))

    for _ in range(days):
        spawn_count = fish.get(0, 0)

        for age in range(8):
            fish[age] = fish.get(age + 1, 0)

        fish[6] += spawn_count
        fish[8] = spawn_count

    return sum(fish.values())


def main():
    with fileinput.input() as input:
        fish = [int(age) for age in list(input)[0].split(",")]

    print(solve(fish))
    print(solve(fish, 256))


if __name__ == "__main__":
    main()
