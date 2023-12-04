import fileinput
import re
from collections import defaultdict


def extract_numbers(string):
    return set(map(int, re.findall(r'\d+', string)))


def parse_card(line):
    card_no, winning, yours = re.match(r'Card +(\d+): ([0-9 ]+) \| ([0-9 ]+)', line).groups()

    card_no = int(card_no)
    winning = extract_numbers(winning)
    yours = extract_numbers(yours)

    return card_no, winning, yours


def match_card(winning, yours):
    return len(winning & yours)


def score_matches(matches):
    return 2 ** (matches - 1) if matches else 0


def part1(data):
    acc = 0
    for line in data:
        _, winning, yours = parse_card(line)

        matches = match_card(winning, yours)

        acc += score_matches(matches)

    return acc

def part2(data):
    cards = defaultdict(int)

    for line in data:
        card_no, winning, yours = parse_card(line)

        matches = match_card(winning, yours)

        cards[card_no] += 1

        matches = (len(winning & yours))

        for offset in range(1, matches + 1):
            cards[card_no + offset] += cards[card_no]

    return sum(cards.values())


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
