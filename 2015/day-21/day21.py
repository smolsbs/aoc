#!/usr/bin/python
import re
import random
import string
from itertools import combinations

WEAPONS = [{"name": "Dagger", "cost": 8, "dmg": 4, "armor": 0},
    {"name": "Shortsword", "cost": 10, "dmg": 5, "armor": 0},
    {"name": "Warhammer", "cost": 25, "dmg": 6, "armor": 0},
    {"name": "Longsword", "cost": 40, "dmg": 7, "armor": 0},
    {"name": "Greataxe", "cost": 74, "dmg": 8, "armor": 0}]

ARMOR = [{"name": "Leather", "cost": 13, "dmg": 0, "armor": 1},
    {"name": "Chainmail", "cost": 31, "dmg": 0, "armor": 2},
    {"name": "Splintmail", "cost": 53, "dmg": 0, "armor": 3},
    {"name": "Bandedmail", "cost": 75, "dmg": 0, "armor": 4},
    {"name": "Platemail", "cost": 102, "dmg": 0, "armor": 5}]
    
RINGS = [{"name": "Damage +1", "cost": 25, "dmg": 1, "armor": 0},
    {"name": "Damage +2", "cost": 50, "dmg": 2, "armor": 0},
    {"name": "Damage +3", "cost": 100, "dmg": 3, "armor": 0},
    {"name": "Defense +1", "cost": 20, "dmg": 0, "armor": 1},
    {"name": "Defense +2", "cost": 40, "dmg": 0, "armor": 2},
    {"name": "Defense +3", "cost": 80, "dmg": 0, "armor": 3}]

class entity:
    def __init__(self, hp, damage, armor):
        self.hp = int(hp)
        self.dmg = int(damage)
        self.armor = int(armor)
        self.items = []
        self.money = 0

    def getDamage(self):
        return self.dmg

    def getCost(self):
        return self.money

    def applyBuff(self, buff):
        for item in buff:
            self.dmg += item['dmg']
            self.armor += item['armor']
            self.money += item['cost']
            self.items.append(item['name'])

    def isAlive(self):
        if self.hp <= 0:
            return False
        else:
            return True

    def printPlayerStats(self):
        return (self.dmg, self.armor, self.items)

    def hit(self, dmg):
        self.hp -= max(1, dmg-self.armor)
        return self.isAlive()

def createPlayers():
    players = []
    comb_rings = []

    for i in range(3):
        rings_i = combinations(RINGS, i)
        for j in rings_i:
            comb_rings.append(j)
    
    # create all players with all possibilites
    for wep in WEAPONS:
        for arm in ARMOR:
            for r in comb_rings:
                p = entity(100, 0, 0)               # create a new player
                p.applyBuff([wep, arm] + list(r))   # apply all buffs from the items
                players.append(p)
            
    return players

def main():
    with open('input', 'r') as fp:
        data = fp.read()
        hp, dmg, armor = re.findall(r'(\d+)', data)

    p_list = createPlayers()
    success = []
    lost = []
    for player in p_list:
        boss = entity(hp, dmg, armor)
        b_alive, p_alive = (True, True)

        for _round in range(30):
            #player goes first, then boss
            b_alive = boss.hit(player.getDamage())
            if not b_alive and p_alive:
                success.append((player.getCost(), player.printPlayerStats()))
                break
            p_alive = player.hit(boss.getDamage())
            if not p_alive:
                lost.append((player.getCost(), player.printPlayerStats()))
                break

    print(sorted(success)[0])
    print(sorted(lost, reverse=True)[0])
        

if __name__ == '__main__':
    main()