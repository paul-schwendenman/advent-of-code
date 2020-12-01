from collections import defaultdict


def load_intial_state(filename='input'):
    state = defaultdict(lambda: defaultdict(bool))

    with open(filename) as file_input:
        lines = file_input.read().splitlines()

    for y, line in enumerate(lines):
        for x, item in enumerate(line):
            state[y][x] = (item == "#")

    return state


def get_neighboors(state, x, y):
    yield state[y-1][x]
    yield state[y][x-1]
    yield state[y+1][x]
    yield state[y][x+1]


def count_neighboors(state, x, y):
    value = 0

    for neighboor in get_neighboors(state, x, y):
        if neighboor:
            value += 1

    return value


def step_simulation(state):
    new_state = defaultdict(lambda: defaultdict(bool))
    for y in range(5):
        for x in range(5):
            space = state[y][x]
            count = count_neighboors(state, x, y)
            if space and count == 1:
                new_state[y][x] = True
            elif not space and count in (1, 2):
                new_state[y][x] = True
    return new_state


def print_grid(state):
    for y in range(5):
        for x in range(5):
            print('#' if state[y][x] else '.', end='')
        print('')
    print('')


def score_state(state):
    score = 0
    count = 0

    for y in range(5):
        for x in range(5):
            if state[y][x]:
                score += pow(2, count)

            count += 1

    return score


def main():
    # intial_state = load_intial_state('input.example')
    intial_state = load_intial_state()

    print_grid(intial_state)
    scores = set()
    score = 0
    state = intial_state

    while True:
        state = step_simulation(state)

        print_grid(state)

        score = score_state(state)
        if score in scores:
            break
        else:
            scores.add(score)

    return score


if __name__ == "__main__":
    print(main())
