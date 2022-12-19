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

class State2(namedtuple('State2', 'location elephant open_valves pressure_released path')):
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
        time_remaining = max_time - time
        print(f'time: {time:2d}\t states: {len(states)}\t best: {len(best)}')

        next_states = []

        for state in states:
            location, open_valves, pressure_released, path = state

            if (key := (location, open_valves)) in best and pressure_released <= best[key]:
                continue

            best[(location, open_valves)] = pressure_released

            if location not in open_valves and valves[location].rate > 0:
                next_states.append(State(location, (open_valves | {location}), pressure_released + (time_remaining) * valves[location].rate, path + [f'{time}: open {location} pressure {calc_pressure_released(valves, open_valves)}']) )
            for neighbor in valves[location].neighbors:
                next_states.append(State(neighbor, open_valves, pressure_released, path+[f'{time}: move {neighbor} pressure {calc_pressure_released(valves, open_valves)}']))

        # states = next_states
        states = next_states if next_states else states

    top_state = sorted(states, key = lambda state: state.pressure_released, reverse=True)

    print(top_state[0].path)

    return top_state[0]


def part1(data, max_time=30, init_open_valves=frozenset(), debug=False):
    valves = dict([parse_line(line) for line in data])

    return solve(valves, max_time).pressure_released


def solve2(valves, max_time):
    states = [State2('AA', 'AA', frozenset(), 0, [])]

    best = {}

    for time in range(1, max_time + 1, 1):
        time_remaining = max_time - time
        print(f'time: {time:2d}\t states: {len(states)}\t best: {len(best)}')

        next_states = []

        for state in states:
            location, elephant, open_valves, pressure_released, path = state

            if (key := (location, elephant, open_valves)) in best and pressure_released <= best[key]:
                continue
            if (key := (elephant, location, open_valves)) in best and pressure_released <= best[key]:
                continue

            best[(location, elephant, open_valves)] = pressure_released

            if location not in open_valves and valves[location].rate > 0:
                location_pressure = time_remaining * valves[location].rate

                if elephant not in open_valves and valves[elephant].rate > 0:
                    if elephant != location:
                        elephant_pressure = time_remaining * valves[elephant].rate
                        next_states.append(State2(location, elephant, (open_valves | {location, elephant}), pressure_released + location_pressure + elephant_pressure, path + [f'{time}: open {location} {elephant}']) )
                for elephant_neighbor in valves[elephant].neighbors:
                    next_states.append(State2(location, elephant_neighbor, open_valves | {location}, pressure_released + location_pressure, path+[f'{time}: open {location} move {elephant_neighbor}']))
            for neighbor in valves[location].neighbors:
                if elephant not in open_valves and valves[elephant].rate > 0:
                    elephant_pressure = time_remaining * valves[elephant].rate
                    next_states.append(State2(neighbor, elephant, (open_valves | {elephant}), pressure_released + elephant_pressure, path + [f'{time}: move {neighbor} open {elephant}']) )
                for elephant_neighbor in valves[elephant].neighbors:
                    next_states.append(State2(neighbor, elephant_neighbor, open_valves, pressure_released, path+[f'{time}: move {neighbor} {elephant_neighbor}']))

        # states = next_states
        states = next_states if next_states else states

    top_state = sorted(states, key = lambda state: state.pressure_released, reverse=True)

    print(top_state[0].path)

    return top_state[0]


def part2(data, max_time=26):
    valves = dict([parse_line(line) for line in data])

    return solve2(valves, max_time).pressure_released
    # valves = dict([parse_line(line) for line in data])

    # print(valves)

    # value = solve(valves, 26)
    # print(value.open_valves)

    # for name in valves:
    #     valves[name].rate = 0

    # print(valves)

    # value2 = solve(valves, 26)

    # return value.pressure_released + value2.pressure_released
    # pass


def main():
    # print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
