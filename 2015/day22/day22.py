import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import dataclasses
import typing
import copy


@dataclasses.dataclass(frozen=True)
class Spell:
    cost: int
    damage: int = 0
    heal: int = 0
    mana: int = 0
    armor: int = 0
    turns: int | None = None

    @property
    def is_effect(self):
        return self.turns is not None


# Magic Missile costs 53 mana. It instantly does 4 damage.
# Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
# Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
# Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
# Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.

spells = {
    Spell(53, damage=4),
    Spell(73, damage=2, heal=2),
    Spell(113, armor=7, turns=6),
    Spell(173, damage=3, turns=3),
    Spell(229, mana=101, turns=5),
}


@dataclasses.dataclass
class Player:
    hit_points: int
    mana: int
    armor: int = 0

    def __iter__(self):
        for field in dataclasses.fields(self):
            yield getattr(self, field.name)


@dataclasses.dataclass
class Boss:
    hit_points: int
    damage: int

    def __iter__(self):
        for field in dataclasses.fields(self):
            yield getattr(self, field.name)


class State(typing.NamedTuple):
    mana_spent: int
    player: Player
    boss: Boss
    effects: typing.Set[Spell]


def part1(data):
    boss, player = Boss(13, 8), Player(10, 250)
    # boss, player = Boss(14, 8), Player(10, 250)
    # boss, player = Boss(51, 9), Player(50, 500)
    lowest_mana = math.inf

    initial_state = State(0, player, boss, set())

    queue: collections.deque[State] = collections.deque([initial_state])

    while len(queue) > 0:
        print(f'states={len(queue)}')
        state = queue.popleft()
        mana_spent, _, _, effects = state

        if mana_spent > lowest_mana:
            continue

        print(f'Available spells: {len(spells - effects)}')
        for spell in spells - effects:
            player = copy.copy(state.player)
            boss = copy.copy(state.boss)

            if spell.cost > player.mana:
                # print(f'Spell too expensive: {spell.cost} > {player.mana}')
                continue
            else:
                # print(f'Casting spell: {spell.cost} < {player.mana}: {mana_spent}')
                player.mana -= spell.cost
                next_mana_spent = mana_spent + spell.cost

                if spell.is_effect:
                    effects.add(Spell)
                else:
                    boss.hit_points -= spell.damage
                    player.hit_points += spell.heal

            if boss.hit_points <= 0:
                print(f'Boss loses')
                lowest_mana = min(lowest_mana, mana_spent)
                continue

            player.hit_points -= min(1, boss.damage - player.armor)

            if player.hit_points <= 0:
                print(f'Player losses')
                continue

            queue.append(State(next_mana_spent, player, boss, effects))


            pass

        pass

    pass


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
