def get_dimensions(description):
    return sorted(int(side) for side in description.split('x'))


def calculate_surface_area(side_a, side_b, side_c):
    return 2 * ((side_a * side_b) + (side_a * side_c) + (side_b * side_c))


def calculate_paper_needed(side_a, side_b, side_c):
    return calculate_surface_area(side_a, side_b, side_c) + (side_a * side_b)


def main():
    pass


if __name__ == "__main__":
    pass
