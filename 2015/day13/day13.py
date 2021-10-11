from itertools import permutations, cycle, islice, tee
import fileinput
import re


def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def parse_rules(rules):
    parser = re.compile(r"(?P<name_1>[A-Za-z]+) would (?P<sign>lose|gain) (?P<value>[0-9]+) happiness units by sitting next to (?P<name_2>[A-Za-z]+).")
    mapping = {}
    names = set()

    for rule in rules:
        values = parser.match(rule)
        name_1 = values["name_1"]
        name_2 = values["name_2"]
        sign = values["sign"]
        value = int(values["value"])

        names.add(name_1)
        names.add(name_2)

        if sign == 'gain':
            mapping[(name_1, name_2)] = value
        else:
            mapping[(name_1, name_2)] = -value


    return names, mapping


def sum_arrangement(arrangement, mapping):
    value = 0
    for name_1, name_2 in islice(pairwise(cycle(arrangement)), len(arrangement)):
        # print(name_1, name_2)
        # print(f"{name_1} -> {name_2} = {mapping[(name_1, name_2)]}")
        # print(f"{name_2} -> {name_1} = {mapping[(name_2, name_1)]}")
        value += mapping[(name_1, name_2)]
        value += mapping[(name_2, name_1)]
    return value


def part1(rules):
    names, mapping = parse_rules(rules)

    # print(mapping)

    max_value = 0

    # for arrangement in [('Alice', 'Bob', 'Carol', 'David')]:
    for arrangement in permutations(names):
        value = sum_arrangement(arrangement, mapping)
        # print(f"{arrangement} {value}")

        if value > max_value:
            max_value = value

    return max_value



def main():
    print(part1(fileinput.input()))


if __name__ == '__main__':
    main()