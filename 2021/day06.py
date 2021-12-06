import fileinput
from collections import Counter, deque, defaultdict, ChainMap


def solve(fish, days=80):
    counts = ChainMap(Counter(fish), defaultdict(int))
    tracker = deque(counts[index] for index in range(9))

    for _ in range(days):
        tracker.rotate(-1)
        tracker[6] += tracker[8]

    return sum(tracker)


def main():
    with fileinput.input() as input:
        fish = [int(age) for age in list(input)[0].split(",")]

    print(solve(fish))
    print(solve(fish, 256))


if __name__ == "__main__":
    main()
