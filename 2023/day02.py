import fileinput

def part1(data):
    goal = {
        'green': 13,
        'blue': 14,
        'red': 12,
    }

    acc = []
    for line in data:
        game, rest = line.split(": ")
        print(game, rest)
        shows = [show.strip() for show in rest.split(';')]
        print(shows)
        colors = [[i.strip().split(' ') for i in j.split(',')] for j in shows]
        print(colors)
        colors = [{color[1]: int(color[0]) for color in j} for j in colors]
        print(colors)

        for set in colors:
            if set.get('green', 0) > goal['green'] or set.get('blue', 0) > goal['blue'] or set.get('red', 0) > goal['red']:
                break
        else:
            acc.append(int(game.split(' ')[1]))


    print(acc)
    return sum(acc)

    pass

def part2(data):
    acc = 0
    for line in data:
        min = {
            'green': 0,
            'blue': 0,
            'red': 0,
        }

        game, rest = line.split(": ")
        print(game, rest)
        shows = [show.strip() for show in rest.split(';')]
        print(shows)
        colors = [[i.strip().split(' ') for i in j.split(',')] for j in shows]
        print(colors)
        colors = [{color[1]: int(color[0]) for color in j} for j in colors]
        print(colors)

        for set in colors:
            if set.get('green', 0) > min['green']:
                min['green'] = set['green']

            if set.get('blue', 0) > min['blue']:
                min['blue'] = set['blue']
            if set.get('red', 0) > min['red']:
                min['red'] = set['red']

        pow = min['blue'] * min['green'] * min['red']
        print(f'{min=}, {pow=}')
        acc += pow



    return acc
    pass

def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
