def get_dimensions(description):
    return sorted(int(side) for side in description.split('x'))


def calculate_surface_area(side_a, side_b, side_c):
    return 2 * ((side_a * side_b) + (side_a * side_c) + (side_b * side_c))


def calculate_paper_needed(side_a, side_b, side_c):
    return calculate_surface_area(side_a, side_b, side_c) + (side_a * side_b)


def calculate_bow_length(side_a, side_b, side_c):
    return side_a * side_b * side_c


def calculate_ribbon_length(side_a, side_b, side_c):
    return 2 * side_a + 2 * side_b + calculate_bow_length(side_a, side_b, side_c)


def main():
    with open("day02/input") as input_file:
        lines = input_file.readlines()

    total = sum(calculate_paper_needed(*get_dimensions(line)) for line in lines)
    print(total)


if __name__ == "__main__":
    main()
