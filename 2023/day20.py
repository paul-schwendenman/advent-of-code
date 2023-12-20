import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing


class Pulse(enum.Enum):
    LOW = enum.auto()
    HIGH = enum.auto()


class ModuleType(enum.Enum):
    FLIPFLOP = enum.auto()
    CONJUNCTION = enum.auto()
    BROADCASTER = enum.auto()

class Module:
    pass

class FlipFlop(Module):
    def __init__(self, dest):
        self.on = True
        self.dest = dest

    def pulse(self, pulse):
        if pulse == Pulse.HIGH:
            return None

        self.on = not self.on

        if self.on:
            return Pulse.HIGH
        else:
            return Pulse.LOW


class Conjunction(Module):
    pass


class Broadcaster(Module):
    pass

class State(typing.NamedTuple):
    name: str
    source: str
    pulse: Pulse


def part1(data):
    tree = {}
    for line in data:
        match = re.match(r'^(broadcaster) -> ((?:[a-z]+, )*[a-z]+)\n$', line)

        if match:
            name, children = match.groups()
            nodes = [child.strip() for child in children.split(',')]
            # print(f'{line=}: {name} {nodes}')

            tree[name] = ModuleType.BROADCASTER, nodes
            continue

        match = re.match(r'^%([a-z]+) -> ((?:[a-z]+, )*[a-z]+)$', line)

        if match:
            name, children = match.groups()
            nodes = [child.strip() for child in children.split(',')]
            # print(f'{line=}: {name} {nodes}')
            tree[name] = ModuleType.FLIPFLOP, nodes
            continue

        match = re.match(r'^&([a-z]+) -> ((?:[a-z]+, )*[a-z]+)$', line)

        if match:
            name, children = match.groups()
            nodes = [child.strip() for child in children.split(',')]
            # print(f'{line=}: {name} {nodes}')
            tree[name] = ModuleType.CONJUNCTION, nodes
            continue

        raise ValueError("No match", line)


    high, low = 0, 0

    modules_memory = collections.defaultdict(lambda: Pulse.LOW)
    modules_input = collections.defaultdict(dict)

    for source, destinations in tree.items():
        print(f'{source=} {destinations=}')
        for destination in destinations[1]:
            modules_input[destination][source] = Pulse.LOW

    # for time in range(1, 2):
    # for time in range(0, 10):
    for time in range(0, 1_000):
        queue = collections.deque([State('broadcaster', 'button', Pulse.LOW)])

        while len(queue) > 0:

            node = queue.popleft()
            name, source, pulse = node
            print(f'name={name}\t source={source}\t pulse={"lo" if pulse == Pulse.LOW else "hi"}')
            print(f'{time+1:4d}: {len(queue)} pulses, {high=} {low=}')

            if pulse == Pulse.HIGH:
                high += 1
            else:
                low += 1

            print(f'{time+1:4d}: {len(queue)} pulses, {high=} {low=}')

            # module_type, nxt_nodes = tree[name]
            module_type, nxt_nodes = tree.get(name, (None, []))

            if module_type is None:
                continue

            if module_type == ModuleType.BROADCASTER:
                next_pulse = pulse

            elif module_type == ModuleType.FLIPFLOP:
                if pulse == Pulse.LOW:
                    if modules_memory[name] == Pulse.HIGH:
                        modules_memory[name] = Pulse.LOW
                    else:
                        modules_memory[name] = Pulse.HIGH

                    next_pulse = modules_memory[name]

                else:
                    continue

            elif module_type == ModuleType.CONJUNCTION:
                modules_input[name][source] = pulse

                print(f'{modules_input[name].values()}')
                if all(pulse == Pulse.HIGH for pulse in modules_input[name].values()):
                    next_pulse = Pulse.LOW
                else:
                    next_pulse = Pulse.HIGH

            for next_node in nxt_nodes:
                queue.append(State(next_node, name, next_pulse))
            print('------')

        if time < 10 or time % 100 == 1:
            print(f'{time:4d}: {low:5d} * {high:5d} = {low * high}')


    print(f'{low} * {high} = {low * high}')
    return high * low


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
