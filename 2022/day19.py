import fileinput
from helper import *
from enum import auto


class State(namedtuple('State', 'ore clay obi geo b_ore b_clay b_obi b_geo')):
    __slots__ = ()

    @classmethod
    def build(cls, supplies, robots):
        return cls(
            supplies[RobotTypes.ORE],
            supplies[RobotTypes.CLAY],
            supplies[RobotTypes.OBSIDEAN],
            supplies[RobotTypes.GEODE],
            robots[RobotTypes.ORE],
            robots[RobotTypes.CLAY],
            robots[RobotTypes.OBSIDEAN],
            robots[RobotTypes.GEODE],
        )

    def extract(self):
        return (
            Counter({
                RobotTypes.ORE: self.ore,
                RobotTypes.CLAY: self.clay,
                RobotTypes.OBSIDEAN: self.obi,
                RobotTypes.GEODE: self.geo,
            }),
            Counter({
                RobotTypes.ORE: self.b_ore,
                RobotTypes.CLAY: self.b_clay,
                RobotTypes.OBSIDEAN: self.b_obi,
                RobotTypes.GEODE: self.b_geo,
            })
        )

class RobotTypes(Enum):
    ORE = auto()
    CLAY = auto()
    OBSIDEAN = auto()
    GEODE = auto()

    def __str__(self):
        return f'{self.name}'


@dataclass
class Blueprint():
    index: int
    ore_robot_ore: int
    clay_robot_ore: int
    obsidian_robot_ore: int
    obsidian_robot_clay: int
    geode_robot_ore: int
    geode_robot_obsidean: int


def parse_blueprint(line):
    values = extract_ints(line)

    assert len(values) == 7

    return Blueprint(*values)



def build_geode_robots(blueprint: Blueprint, state: State):
    supplies, robots = state.extract()
    new_robots = Counter()

    if supplies[RobotTypes.OBSIDEAN] >= blueprint.geode_robot_obsidean and supplies[RobotTypes.ORE] >= blueprint.geode_robot_ore:
        supplies[RobotTypes.OBSIDEAN] -= blueprint.geode_robot_obsidean
        supplies[RobotTypes.ORE] -= blueprint.geode_robot_ore
        robots[RobotTypes.GEODE] += 1

        return State.build(supplies + robots, robots + new_robots)

    return None


def build_obsidean_robots(blueprint: Blueprint, state: State):
    supplies, robots = state.extract()
    new_robots = Counter()

    if supplies[RobotTypes.CLAY] >= blueprint.obsidian_robot_clay and supplies[RobotTypes.ORE] >= blueprint.obsidian_robot_ore:
        supplies[RobotTypes.CLAY] -= blueprint.obsidian_robot_clay
        supplies[RobotTypes.ORE] -= blueprint.obsidian_robot_ore
        robots[RobotTypes.OBSIDEAN] += 1

        return State.build(supplies + robots, robots + new_robots)

    return None

def build_clay_robots(blueprint: Blueprint, state: State):
    supplies, robots = state.extract()
    new_robots = Counter()

    if supplies[RobotTypes.ORE] >= blueprint.clay_robot_ore:
        supplies[RobotTypes.ORE] -= blueprint.clay_robot_ore
        robots[RobotTypes.CLAY] += 1

        return State.build(supplies + robots, robots + new_robots)

    return None


def build_ore_robots(blueprint: Blueprint, state: State):
    supplies, robots = state.extract()
    new_robots = Counter()

    if supplies[RobotTypes.ORE] >= blueprint.ore_robot_ore:
        supplies[RobotTypes.ORE] -= blueprint.ore_robot_ore
        new_robots[RobotTypes.ORE] += 1

        return State.build(supplies + robots, robots + new_robots)

    return None


def build_robots(supplies, blueprint: Blueprint, robots = None):
    if not robots:
        robots = Counter()

    if supplies[RobotTypes.OBSIDEAN] >= blueprint.geode_robot_obsidean and supplies[RobotTypes.ORE] >= blueprint.geode_robot_ore:
        supplies[RobotTypes.OBSIDEAN] -= blueprint.geode_robot_obsidean
        supplies[RobotTypes.ORE] -= blueprint.geode_robot_ore
        robots[RobotTypes.GEODE] += 1
    elif supplies[RobotTypes.OBSIDEAN] >= blueprint.geode_robot_obsidean:
        pass
    elif supplies[RobotTypes.CLAY] >= blueprint.obsidian_robot_clay and supplies[RobotTypes.ORE] >= blueprint.obsidian_robot_ore:
        supplies[RobotTypes.CLAY] -= blueprint.obsidian_robot_clay
        supplies[RobotTypes.ORE] -= blueprint.obsidian_robot_ore
        robots[RobotTypes.OBSIDEAN] += 1
    elif supplies[RobotTypes.CLAY] >= blueprint.obsidian_robot_clay:
        pass
    elif supplies[RobotTypes.ORE] >= blueprint.clay_robot_ore:
        supplies[RobotTypes.ORE] -= blueprint.clay_robot_ore
        robots[RobotTypes.CLAY] += 1
    elif supplies[RobotTypes.ORE] >= blueprint.ore_robot_ore:
        supplies[RobotTypes.ORE] -= blueprint.ore_robot_ore
        robots[RobotTypes.ORE] += 1

    return robots, supplies



def simulate_blueprint(blueprint):
    robots = Counter({
        RobotTypes.ORE: 1,
        # RobotTypes.CLAY: 0,
        # RobotTypes.OBSIDEAN: 0,
        # RobotTypes.GEODE: 0
    })
    supplies = Counter({
        # RobotTypes.ORE: 0,
        # RobotTypes.CLAY: 0,
        # RobotTypes.OBSIDEAN: 0,
        # RobotTypes.GEODE: 0
    })

    states = deque([State.build(supplies, robots)])


    for i in range(24):
        min_potiental = 0
        # min_potiental = max(state.geo + state.b_geo * (24 - i) for state in states)
        print(f'{i}: {len(states)}')

        next_states = deque()


        while states:
            state = states.popleft()
            supplies, robots = state.extract()

            if (potiential := (state.geo + state.b_geo * (24 - i))) < min_potiental:
                continue
            elif potiential > min_potiental:
                min_potiental = potiential
                print(f'best: {potiential}')

            if geode_bot := build_geode_robots(blueprint, state):
                next_states.append(geode_bot)
            if obsidean_bot := build_obsidean_robots(blueprint, state):
                next_states.append(obsidean_bot)
            if clay_bot := build_clay_robots(blueprint, state):
                next_states.append(clay_bot)
            if ore_bot := build_ore_robots(blueprint, state):
                next_states.append(ore_bot)

            next_states.append(State.build(supplies+robots, robots))

        states = next_states

    supplies, _ = sorted(states, key= lambda state: state.geo, reverse=True)[0].extract()


        # print(f'minute {i + 1}\n{robots=}\n{supplies=}\n')
        # new_robots, _ = build_robots(supplies, blueprint)
        # print(f'{new_robots=}\n{supplies=}\n')

        # supplies += robots
        # robots += new_robots

        # print(f'{robots=}\n{supplies=}\n------------\n')
        # # input()
        # pass

    return supplies[RobotTypes.GEODE]


def part1(data):
    blueprints = [parse_blueprint(line) for line in data]

    quality_levels = 0

    for blueprint in blueprints[:]:
        geodes = simulate_blueprint(blueprint)
        print(f'blueprint {blueprint.index} produces {geodes}')

        quality_levels += blueprint.index * geodes

    return quality_levels


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
