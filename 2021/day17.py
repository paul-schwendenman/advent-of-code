import fileinput
from collections import namedtuple
from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class VelocityBounds:
    dx: int
    dy: int

    @property
    def dx_range(self):
        return range(0, self.dx)

    @property
    def dy_range(self):
        return range(-self.dy, self.dy)


@dataclass
class TargetArea:
    x_min: int
    x_max: int
    y_min: int
    y_max: int

    def __str__(self):
        return f'{self.x_min} -> {self.x_max} {self.y_min} -> {self.y_max}'


def parse_target_area(raw: str) -> TargetArea:
    target_area = raw[13:].split(", ")

    [x_min, x_max] = [int(item) for item in target_area[0][2:].split("..")]
    [y_min, y_max] = [int(item) for item in target_area[1][2:].split("..")]

    return TargetArea(x_min, x_max, y_min, y_max)


def find_velocity_bounds(target_area: TargetArea) -> VelocityBounds:
    max_dx = target_area.x_max
    max_dy = max(map(abs, (target_area.y_max, target_area.y_min)))

    return VelocityBounds(max_dx, max_dy)


def fire(dx: int, dy: int, target_area: TargetArea) -> Tuple[bool, Optional[int]]:
    highest_point = -1_000_000_000
    x, y = (0, 0)

    while x < target_area.x_max and y > target_area.y_min:
        x += dx
        y += dy

        dx += -1 if dx > 0 else -1 if dx < 0 else 0
        dy -= 1

        if highest_point < y:
            highest_point = y

        if (
            target_area.x_min <= x <= target_area.x_max
            and target_area.y_min <= y <= target_area.y_max
        ):
            return True, highest_point

    return False, None


def part1(data):
    target_area = parse_target_area(data[0])
    highest_point = -1_000_000_000

    velocity = find_velocity_bounds(target_area)

    for dy in velocity.dy_range:
        for dx in velocity.dx_range:
            hit, new_highest_point = fire(dx, dy, target_area)

            if hit and new_highest_point > highest_point:
                highest_point = new_highest_point
                # target_velocity = dx, dy

    # print(f"target velocity: {target_velocity}")
    # print(f"highest point: {highest_point}")

    return highest_point


def part2(data):
    target_area = parse_target_area(data[0])
    velocities = []

    velocity = find_velocity_bounds(target_area)

    for dy in velocity.dy_range:
        for dx in velocity.dx_range:
            hit, _ = fire(dx, dy, target_area)

            if hit:
                velocities.append((dx, dy))

    return len(velocities)


def main():
    with fileinput.input() as input:
        data = [line.rstrip() for line in input]

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
