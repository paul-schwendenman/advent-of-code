import fileinput
import re
import itertools
import math
import functools
import enum
import collections
import dataclasses


class CardRank(enum.IntEnum):
    JOKER = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


class HandRank(enum.IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_KIND = 6
    FIVE_OF_KIND = 7


def parse_card(card, *, jokers=False):
    if jokers and card == 'J':
        return CardRank.JOKER

    return {
        'A': CardRank.ACE,
        'K': CardRank.KING,
        'Q': CardRank.QUEEN,
        'J': CardRank.JACK,
        'T': CardRank.TEN,
        '9': CardRank.NINE,
        '8': CardRank.EIGHT,
        '7': CardRank.SEVEN,
        '6': CardRank.SIX,
        '5': CardRank.FIVE,
        '4': CardRank.FOUR,
        '3': CardRank.THREE,
        '2': CardRank.TWO
    }[card]


def scoreHand(hand):
    c = collections.Counter(hand)

    best = c.most_common()
    # print(f'{hand=}: {best=} {c=}')

    if best[0][0] == CardRank.JOKER:
        offset = 1
    else:
        offset = 0

    if c[CardRank.JOKER] == 5:
        return HandRank.FIVE_OF_KIND
    elif best[0+offset][1] + c[CardRank.JOKER] == 5:
        return HandRank.FIVE_OF_KIND
    elif best[0+offset][1] + c[CardRank.JOKER] == 4:
        return HandRank.FOUR_OF_KIND
    elif best[0+offset][1] + c[CardRank.JOKER] == 3:
        if best[1+offset][1] == 2:
            return HandRank.FULL_HOUSE
        return HandRank.THREE_OF_KIND
    elif best[0+offset][1] + c[CardRank.JOKER] == 2:
        if best[1+offset][1] == 2:
            return HandRank.TWO_PAIR
        return HandRank.ONE_PAIR
    else:
        return HandRank.HIGH_CARD


def compareHands(hand1, hand2):
    score1, score2 = scoreHand(hand1), scoreHand(hand2)
    if score1 > score2:
        return 1
    elif score2 > score1:
        return -1
    else:
        for c1, c2 in zip(hand1, hand2):
            # cc1 = parse_card(c1)
            # cc2 = parse_card(c2)
            cc1, cc2 = c1, c2
            if cc1 > cc2:
                return 1
            elif cc2 > cc1:
                return -1
        else:
            return 0

def compareHands2(hand, other):
    s1, s2 = scoreHand(hand), scoreHand(other)
    if s1 > s2:
        return 1
    elif s2 > s1:
        return -1
    else:
        for c1, c2 in zip(hand, other):
            # cc1 = parse_card2(c1)
            # cc2 = parse_card2(c2)
            cc1, cc2 = c1, c2
            if cc1 > cc2:
                return 1
            elif cc2 > cc1:
                return -1
        else:
            return 0

def compare_bets(bet1, bet2):
    return compareHands(bet1[0], bet2[0])


def compare_bets2(bet1, bet2):
    return compareHands2(bet1[0], bet2[0])


def parse_line(line, jokers=False):
    hand, bet = line.split(' ')
    cards = [parse_card(card, jokers=jokers) for card in hand]
    return cards, int(bet)

def parse_data(lines, jokers=False):
    return [parse_line(line, jokers=jokers) for line in lines]


def part1(data):
    acc = 0
    for index, (_, bet) in enumerate(sorted(parse_data(data), key=functools.cmp_to_key(compare_bets)), start=1):
        acc += index * bet

    return acc

def part2(data):
    acc = 0
    for index, (_, bet) in enumerate(sorted(parse_data(data, True), key=functools.cmp_to_key(compare_bets2)), start = 1):
        acc += index * bet

    return acc

def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
