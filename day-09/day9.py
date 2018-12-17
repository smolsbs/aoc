#!/usr/bin/env python3
# pylint: disable=C0103, C0111

from collections import defaultdict
from blist import blist
def main(part2=False):
    with open('input', 'r') as fp:
        data = fp.read().split(' ')
    n_players, last_marble = int(data[0]), int(data[6])
    if part2:
        last_marble *= 100
    players = defaultdict(lambda: 0)
    circle = blist([0, 1])
    marble_id = 1
    player_id = 2
    marble_number = 2

    while marble_number <= last_marble:
        if marble_number % 23 == 0:
            players[player_id] += marble_number
            rem_id = ((marble_id - 7 + len(circle) - 1) % len(circle)) + 1
            players[player_id] += circle.pop(rem_id)
            marble_id = rem_id
        else:
            insert_id = (marble_id + 2 - 1) % (len(circle)) + 1
            circle.insert(insert_id, marble_number)
            marble_id = circle.index(marble_number)
        marble_number += 1
        player_id = (player_id + 1) % n_players
    print(max(players.values()))
    return max(players.values())

if __name__ == '__main__':
    main()
    main(True)
