import fileinput
from collections import defaultdict

# def score_cards(winning, yours):
#     # winning = {int(item) for item in winning.strip().split(' ') if item}
#     # yours = {int(item) for item in yours.strip().split(' ') if item}

#     matches = (len(winning & yours))

#     score = 2 ** (matches - 1) if matches else 0

#     return score


def part1(data):
    acc = 0
    for line in data:
        _, rest = line.split(': ')
        winning, yours = rest.split('|')
        # print(f'{winning=}, {yours=}')
        winning = {int(item) for item in winning.strip().split(' ') if item}
        yours = {int(item) for item in yours.strip().split(' ') if item}

        matches = (len(winning & yours))

        score = 2 ** (matches - 1) if matches else 0
        # print(score)
        acc += score

    return acc

def part2(data):
    cards = defaultdict(int)

    acc = 0
    for line in data:
        card, rest = line.split(': ')
        winning, yours = rest.split('|')
        # print(f'{winning=}, {yours=}')
        winning = {int(item) for item in winning.strip().split(' ') if item}
        yours = {int(item) for item in yours.strip().split(' ') if item}
        # print(f'{card=}')
        card = int(card[4:])
        # print(f'{card=}')

        cards[card] += 1

        matches = (len(winning & yours))

        # score = 2 ** (matches - 1) if matches else 0
        # print(f'{score=}')
        # acc += score

        if matches == 0:
            continue

        for i in range(1, matches + 1):
            cards[card + i] += cards[card]

    print(f'{cards=}')

    return sum(cards.values())

    # return acc
    pass

def main():
    # print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
