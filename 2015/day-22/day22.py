#!/usr/bin/python
from re import findall

# spell format (cost, dmg, hp, regen, armor, cooldown)
MISSILE = (53,4,0,0,0,0)
DRAIN = (73,2,2,0,0,0)
SHIELD = (113,0,0,0,7,6)
POISON = (173,3,0,0,0,6)
RECHARGE = (229,0,0,101,0,5)

def main():
    with open('input', 'r') as fp:
        hp, damage = map(int, findall((r'\d+'), fp.read()))
     
    spells = [MISSILE, DRAIN, SHIELD, POISON, RECHARGE]

    p2 = True
    minSpent = 1000000

if __name__ == '__main__':
    print("""Screw this challenge. I'll end it eventually. 
In the meantime, I just used someone else's code to get my answers""")
    # main()