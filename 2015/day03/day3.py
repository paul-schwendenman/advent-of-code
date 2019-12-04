def calculate_houses(path):
    houses = set()
    position = (0, 0)

    houses.add(position)

    for location in path:
        if location == '>':
            x, y = position
            position = x + 1, y
            houses.add(position)
        elif location == '<':
            x, y = position
            position = x - 1, y
            houses.add(position)
        elif location == '^':
            x, y = position
            position = x, y + 1
            houses.add(position)
        elif location == 'v':
            x, y = position
            position = x, y - 1
            houses.add(position)

    return len(houses)
