import fileinput
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


def parse_card(card, *, with_jokers=False):
    if with_jokers and card == 'J':
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


def score_hand(hand: list[CardRank]):
    counter = collections.Counter(hand)
    # jokers = counter[CardRank.JOKER]
    # del counter[CardRank.JOKER]

    best = counter.most_common(2)

    if best[0][1] == 5:
        return HandRank.FIVE_OF_KIND

    if CardRank.JOKER in counter:
        if best[0][0] == CardRank.JOKER:
            target = 1
        else:
            target = 0
        # print(f'1. {counter}=')
        counter[best[target][0]] += counter[CardRank.JOKER]
        # print(f'2. {counter}=')
        del counter[CardRank.JOKER]
        # print(f'3. {counter}=')

    best = counter.most_common(2)

    if best[0][1] == 5:
        return HandRank.FIVE_OF_KIND


    match best[0][1], best[1][1]:
        case 4, 1:
            return HandRank.FOUR_OF_KIND
        case 3, 2:
            return HandRank.FULL_HOUSE
        case 3, 1:
            return HandRank.THREE_OF_KIND
        case 2, 2:
            return HandRank.TWO_PAIR
        case 2, 1:
            return HandRank.ONE_PAIR
        case 1, 1:
            return HandRank.HIGH_CARD

    raise ValueError("No match")


def score_cards(cards_bet, with_jokers=False):
    cards, bet = cards_bet.split(' ')
    hand = [parse_card(card, with_jokers=with_jokers) for card in cards]

    return score_hand(hand), hand, int(bet)


def parse_data(lines, *, with_jokers=False):
    return [score_cards(line, with_jokers=with_jokers) for line in lines]


def hand_to_key(hand):
    return score_hand(hand[0]), hand[0]


def part1(data, with_jokers = False):
    acc = 0
    for index, (_, _, bet) in enumerate(sorted(parse_data(data, with_jokers=with_jokers)), start=1):
        acc += index * bet

    return acc

def part2(data):
    return part1(data, with_jokers=True)

def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
