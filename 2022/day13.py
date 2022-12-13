import fileinput
import functools


def compare(a, b):
    types = type(a), type(b)
    # print(a, b, types)

    if types == (int, int):
        if a < b:
            return True
        elif a > b:
            return False
        return None
    elif types == (list, int):
        return compare(a, [b])
    elif types == (int, list):
        return compare([a], b)
    elif types == (list, list):
        # print('sublist:', len(a), len(b), max(len(a), len(b)))
        for i in range(max(len(a), len(b))):
            if len(a) <= i:
                return True
            elif len(b) <= i:
                return False
            else:
                sub = compare(a[i], b[i])

                if sub is None:
                    continue
                return sub
    else:
        raise ValueError("Types: %s", types)


def part1(data):
    pairs = (tuple(eval(pairing.strip()) for pairing in pair.split('\n')) for pair in ''.join(data).strip().split('\n\n'))
    count = 0
    correct_pairs = []

    for i, pair in enumerate(pairs):
        if result := compare(*pair):
            count += 1
            correct_pairs.append(i)
        print(i, pair, result)

    return sum(correct_pairs) + len(correct_pairs)
    pass


def part2(data):
    packets = [eval(packet) for packet in data if packet.strip()] + [[[2]], [[6]]]

    a = sum(1 for packet in packets if compare(packet, [[2]])) + 1
    b = sum(1 for packet in packets if compare(packet, [[6]])) + 1

    return a * b


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
