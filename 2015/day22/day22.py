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


class Turn(enum.Enum):
    PLAYER = 0
    BOSS = 1

    def __str__(self):
        return 'Player' if self == Turn.PLAYER else 'Boss'

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
    player_hp: int
    player_mana: int
    boss_hp: int
    mana_spent: int = 0
    turn: Turn = Turn.PLAYER
    poison_left: int = 0
    shield_left: int = 0
    recharge_left: int = 0
    messages: list[str] = []


def part1(data):
    # boss, player = Boss(6, 8), Player(10, 250)
    # boss, player = Boss(13, 8), Player(10, 250)
    # boss, player = Boss(14, 8), Player(10, 250)
    boss, player = Boss(51, 9), Player(50, 500)
    lowest_mana = math.inf

    initial_state = State(player_hp=player.hit_points, player_mana=player.mana, boss_hp=boss.hit_points)

    queue: collections.deque[State] = collections.deque([initial_state])

    while len(queue) > 0:
        # print(f'states={len(queue)}')
        state = queue.popleft()
        player_hp, mana, boss_hp, mana_spent, turn, poison_left, shield_left, recharge_left, messages = state
        player_armor = 0
        messages.append(f'-- {turn} turn --')
        messages.append(f'- Player has {player_hp} hit points, {7 if shield_left else 0} armor, {mana} mana')
        messages.append(f'- Boss has {boss_hp} hit points')

        if turn == Turn.PLAYER:
            player_hp -= 1
        if player_hp == 0:
            continue

        if mana < 0:
            # print('pruning, out of mana')
            continue
            pass

        if boss_hp <= 0:
            # print('--------------------------a')
            # for i in m:
            #     print(i)
            # print('')
            print(f'boss loses: {mana_spent} < {lowest_mana} left {mana}')
            if mana_spent < lowest_mana:
                lowest_mana = mana_spent
            continue


        if mana_spent > lowest_mana:
            # print(f'pruning {mana_spent} > {lowest_mana}')
            continue
            pass

        if player_hp <= 0:
            raise ValueError('player hp')

        if poison_left:
            poison_left -= 1
            boss_hp -= 3 #magic
            messages.append(f'Poison deals 3 damage; its timer is now {poison_left}.')
            messages.append(f'Boss now has {boss_hp} hp')

            if boss_hp <= 0:
                print(f'boss hp zzz: {boss_hp} {poison_left}')
                # print('--------------------------b')
                # for i in messages:
                #     print(i)
                # print('')
                print(f'boss loses: {mana_spent} < {lowest_mana} left {mana}')
                if mana_spent < lowest_mana:
                    lowest_mana = mana_spent
                continue

        if shield_left:
            shield_left -= 1
            player_armor = 7 #magic
            messages.append(f'Shield\'s timer is now {shield_left}.')

        if recharge_left:
            recharge_left -= 1
            mana += 101 #magic
            messages.append(f'Recharge provides 101 mana; its timer is now {recharge_left}.')
            messages.append(f'Player now has {mana} mana')

        if turn == Turn.PLAYER:
            for spell in spells:
                n_player_hp = player_hp
                n_boss_hp = boss_hp
                n_mana = mana - spell.cost
                n_mana_spent = mana_spent + spell.cost
                n_poison_left, n_shield_left, n_recharge_left = poison_left, shield_left, recharge_left

                m = copy.copy(messages)
                if spell.turns and spell.armor and shield_left:
                    continue
                elif spell.turns and spell.damage and poison_left:
                    continue
                elif spell.turns and spell.mana and recharge_left:
                    continue

                if spell.cost == 73: #magic
                    m.append('Player casts Drain, dealing 2 damage, and healing 2 hit points.')
                    n_player_hp += 2
                    n_boss_hp -= 2
                elif spell.cost == 53: #magic
                    m.append('Player casts Magic Missile, dealing 4 damage.')
                    n_boss_hp -= 4
                elif spell.cost == 113:
                    m.append('Player casts Shield, increasing armor by 7.')
                    n_shield_left = 6
                elif spell.cost == 173:
                    m.append('Player casts Poison.')
                    n_poison_left = 6
                elif spell.cost == 229:
                    m.append('Player casts Recharge.')
                    n_recharge_left = 5
                else:
                    raise ValueError('huh')

                m.append(f'Spell costs {spell.cost} mana')

                # if n_boss_hp <= 0:
                #     print('---------------')
                #     for i in m:
                #         print(i)
                #     print(f'boss loses: {n_mana_spent} < {lowest_mana}')
                #     print(f'{boss_hp} -> {n_boss_hp}')
                #     if n_mana_spent < lowest_mana:
                #         lowest_mana = n_mana_spent
                #     continue

                m.append('')
                queue.append(State(n_player_hp, n_mana, n_boss_hp, n_mana_spent, Turn.BOSS, n_poison_left, n_shield_left, n_recharge_left, m))
        else:
            player_hp -= max(1, boss.damage - player_armor)
            messages.append(f'Boss attacks for {boss.damage} - {player_armor} = {max(1, boss.damage - player_armor)} damage!')

            if player_hp <= 0:
                # print('---------------')
                # for i in messages:
                #     print(i)
                # print('player loses')
                continue

            messages.append('')
            queue.append(State(player_hp, mana, boss_hp, mana_spent, Turn.PLAYER, poison_left, shield_left, recharge_left, messages))


            pass

        pass

    return lowest_mana


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
