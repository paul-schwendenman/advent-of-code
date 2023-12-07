import fileinput
import re
import itertools
import math
import functools
import enum
import collections

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


def parse_card(card):
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

def parse_card2(card):
    return {
        'A': CardRank.ACE,
        'K': CardRank.KING,
        'Q': CardRank.QUEEN,
        'J': CardRank.JOKER,
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
    # print(f'{best=}')

    if best[0][1] == 5:
        return HandRank.FIVE_OF_KIND
    elif best[0][1] == 4:
        return HandRank.FOUR_OF_KIND
    elif best[0][1] == 3:
        if best[1][1] == 2:
            return HandRank.FULL_HOUSE
        return HandRank.THREE_OF_KIND
    elif best[0][1] == 2:
        if best[1][1] == 2:
            return HandRank.TWO_PAIR
        return HandRank.ONE_PAIR
    else:
        return HandRank.HIGH_CARD

def scoreHand2(hand):
    c = collections.Counter(hand)

    best = c.most_common()
    print(f'{hand=}: {best=} {c=}')

    if best[0][0] == 'J':
        offset = 1
    else:
        offset = 0

    if c['J'] == 5:
        return HandRank.FIVE_OF_KIND
    elif best[0+offset][1] + c['J'] == 5:
        return HandRank.FIVE_OF_KIND
    elif best[0+offset][1] + c['J'] == 4:
        return HandRank.FOUR_OF_KIND
    elif best[0+offset][1] + c['J'] == 3:
        if best[1+offset][1] == 2:
            return HandRank.FULL_HOUSE
        return HandRank.THREE_OF_KIND
    elif best[0+offset][1] + c['J'] == 2:
        if best[1+offset][1] == 2:
            return HandRank.TWO_PAIR
        return HandRank.ONE_PAIR
    else:
        return HandRank.HIGH_CARD


def compareHands(hand, other):
    s1, s2 = scoreHand(hand), scoreHand(other)
    if s1 > s2:
        return 1
    elif s2 > s1:
        return -1
    else:
        for c1, c2 in zip(hand, other):
            cc1 = parse_card(c1)
            cc2 = parse_card(c2)
            if cc1 > cc2:
                return 1
            elif cc2 > cc1:
                return -1
        else:
            return 0

def compareHands2(hand, other):
    s1, s2 = scoreHand2(hand), scoreHand2(other)
    if s1 > s2:
        return 1
    elif s2 > s1:
        return -1
    else:
        for c1, c2 in zip(hand, other):
            cc1 = parse_card2(c1)
            cc2 = parse_card2(c2)
            if cc1 > cc2:
                return 1
            elif cc2 > cc1:
                return -1
        else:
            return 0


def part1(data):
    acc = 0
    for index, (hand, bet) in enumerate(sorted((item.split(' ') for item in data), key=functools.cmp_to_key(lambda a, b: compareHands(a[0], b[0])))):
        bet = int(bet)
        score = scoreHand(hand)

        print(f'{index=} {score=} {hand=}')
        acc += (index+1) * bet

    CardRank.FIVE
    pass
    return acc

def part2(data):
    acc = 0
    for index, (hand, bet) in enumerate(sorted((item.split(' ') for item in data), key=functools.cmp_to_key(lambda a, b: compareHands2(a[0], b[0])))):
        bet = int(bet)
        score = scoreHand(hand)

        print(f'{index=} {score=} {hand=}')
        acc += (index+1) * bet

    CardRank.FIVE
    pass
    return acc
    pass

def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
