#!/usr/bin/python
import random
from re import findall

MAX_ROUNDS = 30
SPELL = {"Magic Missile": {"cooldown": 0, "mana_cost": 53, "dmg": 4, "effect": None},
    "Drain": {"cooldown": 0, "mana_cost": 73, "dmg": 2, "effect": 2},
    "Shield": {"cooldown": 6, "mana_cost": 113, "dmg": 0, "effect": 7},
    "Poison": {"cooldown": 6, "mana_cost": 173, "dmg": 0, "effect": 2},
    "Recharge": {"cooldown": 5, "mana_cost": 229, "dmg": 0, "effect": 101}}


def isEntityDead(entity):
    if entity['hp'] <= 0:
        return True
    return False

def intersect(l1, l2):
    if len(l2) != 0:
        return [v for v in l1 if v in l2]
    return ["Magic Missile", "Drain"]


def main():
    with open('input', 'r') as fp:
        hp, damage = map(int, findall((r'\d+'), fp.read()))


    succ = []

    for p in range(10000):
        boss = {"hp": hp, "dmg": damage}
        player = {"hp": 50, "mana": 500, "spent": 0, "armor": 0, "cds": {}}

        avalEffects = {"Shield", "Poison", "Recharge"}
        print("player {}".format(p))

        for r in range(MAX_ROUNDS):
            print("\tRound {}".format(r+1))
            # player move
            # tick any effect first, then apply a new spell
            if len(player['cds']) > 0:
                for e in player['cds']:
                    if e == "Poison" and player['cds'][e] > 0:
                        boss['hp'] -= SPELL[e]['effect']
                        player['cds'][e] -= 1
                        print("\t\tPoison ticked.")
                    elif e == "Shield" and player['cds'][e] > 0:
                        player['cds'][e] -= 1
                        print("\t\tShield ticked.")
                    elif e == "Recharge" and player['cds'][e] > 0:
                        player['mana'] += SPELL[e]['effect']
                        player['cds'][e] -= 1
                        print("\t\tRecharge ticked.")

                    if player['cds'][e] == 0:
                        if e == "Shield":
                            player['armor'] = 0
                        avalEffects.add(e)

            if isEntityDead(boss):
                succ.append(player['spent'])
                break

            # select new spell, check if mana is avaliable and attack
            e = random.choice(intersect(list(SPELL.keys()), avalEffects))

            print("\t\tAttacking boss with spell {}".format(e))

            if player['mana'] < SPELL[e]['mana_cost']:
                print("\tNot enough mana. Player lost")
                break
            player['mana'] -=  SPELL[e]['mana_cost']
            player['spent'] += SPELL[e]['mana_cost']

            if e  == "Magic Missile":
                boss['hp'] -= SPELL[e]['dmg']
                
            elif e == "Drain":
                boss['hp'] -= SPELL[e]['dmg']
                player['hp'] += SPELL[e]['effect']
            elif e == "Shield":
                player['cds'][e] = SPELL[e]['cooldown']
                player['armor'] = SPELL[e]['effect']
                avalEffects.remove(e)
            elif e == "Poison":
                player['cds'][e] = SPELL[e]['cooldown']
                boss['hp'] -= SPELL[e]['dmg']
                avalEffects.remove(e)
            elif e == "Recharge":
                player['cds'][e] = SPELL[e]['cooldown']
                player['mana'] += SPELL[e]['effect']
                avalEffects.remove(e)
            

            if isEntityDead(boss):
                print("\tBoss killed. Adding player to success cases")
                succ.append(player['spent'])
                break
            
            # boss move

            player['hp'] -= max(1, boss['dmg'] - player['armor'])
            if isEntityDead(player):
                print("\t\tPlayer died")
                break

            print("\t\tBoss attacked")
            
            print("\tEnd of round. Boss HP: {}\tPlayer HP & mana: {} {}".format(boss['hp'], player['hp'], player['mana']))

    print(sorted(succ)[0])

if __name__ == '__main__':
    main()