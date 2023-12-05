import fileinput
import re
from collections import defaultdict, namedtuple
from itertools import islice
from tqdm import tqdm


def batched(iterable, n):
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch

class Transform(namedtuple('Transform', 'range delta')):
    __slots__ = ()


def extract_ints(string):
    return list(map(int, re.findall('\d+', string)))


def part1(data):
    seeds = []
    maps = defaultdict(lambda: defaultdict(list))

    seeds = extract_ints(next(data))
    # print(f'{seeds=}')

    assert '\n' == next(data)

    try:
        while True:
            line = next(data)
            # print(f'{line=}')
            source_name, dest_name = re.match(r'([a-z]+)-to-([a-z]+) map:\n', line).groups()

            # print(f'{source_name=} {dest_name=}')
            while True:
                line = next(data)
                # print(f'{line=}')
                if line == '\n':
                    break

                # source_start, dest_start, range_length = extract_ints(line)
                dest_start, source_start, range_length = extract_ints(line)
                # print(f'{source_start=} {dest_start=} {range_length=}')

                source_end = source_start + range_length + 1
                source_range = range(source_start, source_end)
                delta = dest_start - source_start


                # for offset in range(range_length):
                #     maps[source_name][dest_name][source_start + offset] = dest_start + offset
                maps[source_name][dest_name].append(Transform(source_range, delta))

            # break
    except Exception as e:
        print(e)
    pass
    # print(f'{maps["seed"]["soil"]}')
    # print(f'{maps["soil"]["fertilizer"]}')
    for src, dest in (
        ('seed', 'soil'),
        ('soil', 'fertilizer'),
        ('fertilizer', 'water'),
        ('water', 'light'),
        ('light', 'temperature'),
        ('temperature', 'humidity'),
        ('humidity', 'location')
    ):
        print(f'{src}->{dest}:\t\t{maps[src][dest]}')

    locations = []
    for seed in seeds:
        value = seed
        for src, dest in (
            ('seed', 'soil'),
            ('soil', 'fertilizer'),
            ('fertilizer', 'water'),
            ('water', 'light'),
            ('light', 'temperature'),
            ('temperature', 'humidity'),
            ('humidity', 'location')
        ):
            # value = maps[src][dest].get(value, value)
            # print(f'{src} {value} to {dest}:')
            for transform in maps[src][dest]:
                if value in transform.range:
                    # print(f'{src} {value} to {dest}: {value + transform.delta}')
                    value += transform.delta
                    break
            else:
                # print(f'{src} {value} to {dest}: {value}')
                value = value
        # print(f'location={value}')
        locations.append(value)
        # print()

    print(f'{locations=}')
    return min(locations)


def make_seeds(seed_pairs):
    for start, length in seed_pairs:
        for offset in range(length, step=10_000):
            yield start + offset

def make_sparse_seeds(seed_pairs):
    for start, length in seed_pairs:
        for offset in range(length, step=10_000):
            yield start + offset

def part2(data):
    seeds = []
    seed_map = {}
    maps = defaultdict(lambda: defaultdict(list))

    seed_pairs = list(batched(extract_ints(next(data)), 2))
    # print(f'{seeds=}')

    assert '\n' == next(data)

    try:
        while True:
            line = next(data)
            # print(f'{line=}')
            source_name, dest_name = re.match(r'([a-z]+)-to-([a-z]+) map:\n', line).groups()

            # print(f'{source_name=} {dest_name=}')
            while True:
                line = next(data)
                # print(f'{line=}')
                if line == '\n':
                    break

                # source_start, dest_start, range_length = extract_ints(line)
                dest_start, source_start, range_length = extract_ints(line)
                # print(f'{source_start=} {dest_start=} {range_length=}')

                source_end = source_start + range_length + 1
                source_range = range(source_start, source_end)
                delta = dest_start - source_start


                # for offset in range(range_length):
                #     maps[source_name][dest_name][source_start + offset] = dest_start + offset
                maps[source_name][dest_name].append(Transform(source_range, delta))

            # break
    except Exception as e:
        print(e)
    pass
    # print(f'{maps["seed"]["soil"]}')
    # print(f'{maps["soil"]["fertilizer"]}')
    # for src, dest in (
    #     ('seed', 'soil'),
    #     ('soil', 'fertilizer'),
    #     ('fertilizer', 'water'),
    #     ('water', 'light'),
    #     ('light', 'temperature'),
    #     ('temperature', 'humidity'),
    #     ('humidity', 'location')
    # ):
    #     print(f'{src}->{dest}:\t\t{maps[src][dest]}')

    locations = []
    # for seed in tqdm(make_seeds(seed_pairs), total=2398198298):
    for seed in tqdm(make_sparse_seeds(seed_pairs)):
        value = seed
        for src, dest in (
            ('seed', 'soil'),
            ('soil', 'fertilizer'),
            ('fertilizer', 'water'),
            ('water', 'light'),
            ('light', 'temperature'),
            ('temperature', 'humidity'),
            ('humidity', 'location')
        ):
            # value = maps[src][dest].get(value, value)
            # print(f'{src} {value} to {dest}:')
            for transform in maps[src][dest]:
                if value in transform.range:
                    # print(f'{src} {value} to {dest}: {value + transform.delta}')
                    value += transform.delta
                    break
            else:
                # print(f'{src} {value} to {dest}: {value}')
                value = value
        # print(f'location={value}')
        locations.append(value)
        seed_map[value] = seed
        # print()

    # print(f'{locations=}')
    # print(len(list(make_seeds(seed_pairs))))
    rough_location =  min(locations)

    for start, length in seed_pairs:
        print(f'seed: {seed_map[rough_location]}')
        if start <= seed_map[rough_location] <= start + length:
            print(f'{start=} {length=}')
            break
    else:
        raise ValueError("Not found")


    locations = []
    for seed in tqdm(range(start, start + length), total=length):
        value = seed
        for src, dest in (
            ('seed', 'soil'),
            ('soil', 'fertilizer'),
            ('fertilizer', 'water'),
            ('water', 'light'),
            ('light', 'temperature'),
            ('temperature', 'humidity'),
            ('humidity', 'location')
        ):
            # value = maps[src][dest].get(value, value)
            # print(f'{src} {value} to {dest}:')
            for transform in maps[src][dest]:
                if value in transform.range:
                    # print(f'{src} {value} to {dest}: {value + transform.delta}')
                    value += transform.delta
                    break
            else:
                # print(f'{src} {value} to {dest}: {value}')
                value = value
        # print(f'location={value}')
        locations.append(value)
        # print()

    print(f'{locations=}')
    return min(locations)


    pass

def main():
    # print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
