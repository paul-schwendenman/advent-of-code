import fileinput
from collections import Counter

class Fish:
    def __init__(self, age=8):
        self._age = age
        self._children = []

    def age(self):
        self._age -= 1

        if self._age < 0:
            self._children.append(Fish())
            self._age = 6

    def children(self):
        self._children, out = [], self._children

        return out

class FishTwo:
    def __init__(self, age=8, count=1):
        self._age = age
        self._children = []

    def age(self):
        self._age -= 1

        if self._age < 0:
            self._children.append(Fish())
            self._age = 6

    def children(self):
        self._children, out = [], self._children

        return out


def part1(fish):
    fish = list(map(Fish, fish))

    for i in range(80):
        print(f'day {i}: {len(fish)} fish')
        new = []
        for a_fish in fish:
            a_fish.age()
            new.extend(a_fish.children())

        fish.extend(new)

    return len(fish)
    pass

def part2(fish):
    fish = dict(Counter(fish))

    for i in range(256):
        # print(f'day {i}: {sum(fish.values())} fish')
        spawn_count = fish.get(0, 0)
        fish[0] = fish.get(1, 0)
        fish[1] = fish.get(2, 0)
        fish[2] = fish.get(3, 0)
        fish[3] = fish.get(4, 0)
        fish[4] = fish.get(5, 0)
        fish[5] = fish.get(6, 0)
        fish[6] = fish.get(7, 0) + spawn_count
        fish[7] = fish.get(8, 0)
        fish[8] = spawn_count

    return sum(fish.values())


def main():
    with fileinput.input() as input:
        fish = [int(age) for age in list(input)[0].split(',')]

    # print(part1(fish))
    print(part2(fish))

if __name__ == '__main__':
    main()
