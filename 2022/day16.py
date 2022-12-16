import fileinput
from helper import *


@dataclass
class Valve:
    name: str
    rate: int
    # open: bool = field(default = False, init=False)
    neighbors: list = field(default_factory=list)


class State(namedtuple('State', 'location open_valves pressure_released path')):
    __slots__ = ()


def parse_line(line):
    first, second = line.split(';')
    valve = first[6:8]
    rate = int(first.split('=')[1])

    paths = [item[:2] for item in second.split(' ')[5:]]

    return valve, Valve(valve, rate, neighbors = paths)


def calc_pressure_released(valves, open_valves):
    # print([valve.rate for valve in valves.values() if valve.name in open_valves])
    return sum(valve.rate for valve in valves.values() if valve.name in open_valves)


def solve(valves, max_time):
    states = [State('AA', frozenset(), 0, [])]

    best = {}

    for time in range(1, max_time + 1, 1):
        print(f'time: {time:2d}\t states: {len(states)}\t best: {len(best)}')

        next_states = []

        for state in states:
            location, open_valves, pressure_released, path = state

            if (key := (location, open_valves)) in best and pressure_released <= best[key]:
                continue

            best[(location, open_valves)] = pressure_released

            if location not in open_valves and valves[location].rate > 0:
                next_states.append(State(location, (open_valves | {location}), pressure_released + (max_time - time) * valves[location].rate, path + [f'{time}: open {location} pressure {calc_pressure_released(valves, open_valves)}']) )
            for neighbor in valves[location].neighbors:
                next_states.append(State(neighbor, open_valves, pressure_released, path+[f'{time}: move {neighbor} pressure {calc_pressure_released(valves, open_valves)}']))

        states = next_states

    # return max(state.pressure_released for state in states)
    top = max(state.pressure_released for state in states)

    # for state in states:
    #     if state.pressure_released == top:
    #         print(state.path)
    #         break

    return top, open_valves


def part1(data, max_time=30, init_open_valves=frozenset(), debug=False):
    valves = dict([parse_line(line) for line in data])

    return solve(valves, max_time)[0]



def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
