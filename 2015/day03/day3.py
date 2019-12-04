def calculate_houses(path):
    houses = set()
    position = (0, 0)

    houses.add(position)

    for location in path:
        if location == '>':
            x, y = position
            position = x + 1, y
            houses.add(position)

    return len(houses)
