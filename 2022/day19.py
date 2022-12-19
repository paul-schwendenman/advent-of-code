import fileinput
from helper import *
from enum import auto


class State(namedtuple('State', 'ore cla obi geo b_ore b_clay b_obi b_geo')):
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
                RobotTypes.CLAY: self.cla,
                RobotTypes.OBSIDEAN: self.obi,
                RobotTypes.GEODE: self.geo,
            }),
            Counter({
                RobotTypes.ORE: self.b_ore,
                RobotTypes.CLAY: self.b_cla,
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


def build_robots(supplies, blueprint: Blueprint, robots = None):
    if not robots:
        robots = Counter()

    if supplies[RobotTypes.OBSIDEAN] >= blueprint.geode_robot_obsidean and supplies[RobotTypes.ORE] >= blueprint.geode_robot_ore:
        supplies[RobotTypes.OBSIDEAN] -= blueprint.geode_robot_obsidean
        supplies[RobotTypes.ORE] -= blueprint.geode_robot_ore
        robots[RobotTypes.GEODE] += 1
    elif supplies[RobotTypes.CLAY] >= blueprint.obsidian_robot_clay and supplies[RobotTypes.ORE] >= blueprint.obsidian_robot_ore:
        supplies[RobotTypes.CLAY] -= blueprint.obsidian_robot_clay
        supplies[RobotTypes.ORE] -= blueprint.obsidian_robot_ore
        robots[RobotTypes.OBSIDEAN] += 1
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


    for i in range(24):
        print(f'minute {i + 1}\n{robots=}\n{supplies=}\n')
        new_robots, _ = build_robots(supplies, blueprint)
        print(f'{new_robots=}\n{supplies=}\n')

        supplies += robots
        robots += new_robots

        print(f'{robots=}\n{supplies=}\n------------\n')
        # input()
        pass

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
