import fileinput

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

def main():
    with fileinput.input() as input:
        fish = [int(age) for age in list(input)[0].split(',')]

    print(part1(fish))

if __name__ == '__main__':
    main()
