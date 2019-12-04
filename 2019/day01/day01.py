import math
import sys


def calculate_fuel_fuel(module_mass):
    if module_mass > 0:
        fuel = calculate_fuel(module_mass)
        return fuel + calculate_fuel_fuel(fuel)
    else:
        return 0


def calculate_fuel(module_mass):
    return max(math.floor(module_mass / 3) - 2, 0)


def main(filename):
    lines = []
    with open(filename) as file:
        lines = file.readlines()

    return sum(calculate_fuel_fuel(int(item)) for item in lines)


if __name__ == '__main__':
    print(main(sys.argv[1]))
