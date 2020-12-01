from collections import defaultdict


def load_intial_state(filename='input'):
    state = defaultdict(lambda: defaultdict(bool))

    with open(filename) as file_input:
        lines = file_input.read().splitlines()

    for y, line in enumerate(lines):
        for x, item in enumerate(line):
            state[y][x] = (item == "#")

    return state


def get_neighboors_above(states, x, y, depth):
    if x == 0:
        yield states[depth][2][1]
    elif x == 4:
        yield states[depth][2][3]
    if y == 0:
        yield states[depth][1][2]
    elif y == 4:
        yield states[depth][3][2]


def get_neighboors_below(states, x, y, depth):
    if x == 2 and y == 1:
        yield from [states[depth][0][x] for x in range(5)]
    elif x == 2 and y == 3:
        yield from [states[depth][4][x] for x in range(5)]
    elif x == 1 and y == 2:
        yield from [states[depth][y][0] for y in range(5)]
    elif x == 3 and y == 2:
        yield from [states[depth][y][4] for y in range(5)]


def get_neighboors(states, x, y, depth):
    yield states[depth][y-1][x]
    yield states[depth][y][x-1]
    yield states[depth][y+1][x]
    yield states[depth][y][x+1]
    yield from get_neighboors_above(states, x, y, depth - 1)
    yield from get_neighboors_below(states, x, y, depth + 1)


def count_neighboors(states, x, y, depth):
    value = 0

    for neighboor in get_neighboors(states, x, y, depth):
        if neighboor:
            value += 1

    return value


def step_simulation(states):
    new_states = defaultdict(lambda: defaultdict(lambda: defaultdict(bool)))
    for depth in range(-200, 200):
        state = states[depth]
        for y in range(5):
            for x in range(5):
                if y == 2 and x == 2:
                    continue
                space = state[y][x]
                count = count_neighboors(states, x, y, depth)
                if space and count == 1:
                    new_states[depth][y][x] = True
                elif not space and count in (1, 2):
                    new_states[depth][y][x] = True
    return new_states


def print_grid(states):
    for depth, state in states.items():
        print(f'depth {depth}:')
        for y in range(5):
            for x in range(5):
                if y == 2 and x == 2:
                    print('?', end='')
                else:
                    print('#' if state[y][x] else '.', end='')
            print('')
        print('')
    print('')


def count_bugs(states):
    count = 0

    for depth, state in states.items():
        for y in range(5):
            for x in range(5):
                if state[y][x]:
                    count += 1

    return count


def main():
    # initial_state = load_intial_state('input.example')
    initial_state = load_intial_state()
    states = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

    score = 0
    states[0] = initial_state
    print_grid(states)

    for _ in range(200):
        states = step_simulation(states)

        print_grid(states)
        print('__________________________')

        score = count_bugs(states)

    return score


if __name__ == "__main__":
    print(main())
