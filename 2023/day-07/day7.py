#!/usr/bin/env python3

import aocUtils
from collections import Counter


def run(path):
    data = aocUtils.loadInput(f"{path}/input")

    hands = sort_by_hand(data)
    hands_p2 = sort_by_hand_p2(data)

    p1 = calculate_winnings(hands)
    p2 = calculate_winnings(hands_p2)

    return (p1, p2)


def calculate_winnings(hands: list[tuple[int,str,int]]) -> int:
    winnings = 0
    for idx, v in enumerate(hands):
        winnings += (idx+1) * v[2]

    return winnings


def sort_by_hand(data:list[str]) -> list[tuple[int,str,int]]:
    hands = []
    for hand in data:
        hands.append(group_by(hand))

    for i in range(0, len(hands)-1):
        min_v = hands[i]
        pos_min = i
        for j in range(i, len(hands)):
            if check_two(min_v, hands[j]):
                min_v = hands[j]
                pos_min = j
        if pos_min == i:
            continue

        aux = hands[i]
        hands[i] = hands[pos_min]
        hands[pos_min] = aux
    
    return hands


def sort_by_hand_p2(data:list[str]) -> list[tuple[int,str,int]]:
    hands = []
    for hand in data:
        hands.append(group_by_part2(hand))

    for i in range(0, len(hands)-1):
        min_v = hands[i]
        pos_min = i
        for j in range(i, len(hands)):
            if check_two_p2(min_v, hands[j]):
                min_v = hands[j]
                pos_min = j
        if pos_min == i:
            continue

        aux = hands[i]
        hands[i] = hands[pos_min]
        hands[pos_min] = aux
    
    return hands


def check_two(card1, card2):
    if card1[0] < card2[0]:
        return True
    if card1[0] > card2[0]:
        return False

    for c in zip(list(card1[1]), list(card2[1])):
        if get_card_value(c[0]) > get_card_value(c[1]):
            return True
        elif get_card_value(c[0]) < get_card_value(c[1]):
            return False
    
    return True


def check_two_p2(card1, card2):
    if card1[0] < card2[0]:
        return True
    if card1[0] > card2[0]:
        return False
    
    # we are now on the same type of hand

    for c in zip(list(card1[1]), list(card2[1])):
        if get_card_value_p2(c[0]) > get_card_value_p2(c[1]):
            return True
        elif get_card_value_p2(c[0]) < get_card_value_p2(c[1]):
            return False
    
    return True


def group_by(line: str) -> tuple[int, str, int]:
    cards, bid = line.split(" ")
    aux = dict(Counter(cards))
    card_count = list(sorted(aux.items(),reverse=True, key=lambda x: x[1]))
    l = len(card_count)

    if l == 1:
        t = 1       # five of a kind
    elif l == 2 and card_count[0][1] == 4:
        t = 2       # four of a kind
    elif card_count[0][1] == 3 and card_count[1][1] == 2:
        t = 3       # full house
    elif card_count[0][1] == 3 and card_count[1][1] == 1:
        t = 4       # three of a kind
    elif card_count[0][1] == 2 and card_count[1][1] == 2:
        t = 5        # two pairs
    elif l == 4 and card_count[0][1] == 2:
        t = 6       # one pair 
    else:
        t = 7       # high card

    return (t, cards, int(bid))


def group_by_part2(line: str) -> tuple[int, str, int]:
    cards, bid = line.split(" ")
    aux = dict(Counter(cards))
    if 'J' in aux.keys() and aux['J'] != 5:
        joker_n = aux['J']
        del(aux['J'])
        biggest = sorted(aux.items(), reverse=True, key=lambda x: x[1])[0][0]
        aux[biggest] += joker_n

    card_count = list(sorted(aux.items(),reverse=True, key=lambda x: x[1]))
    l = len(card_count)

    if l == 1:
        t = 1       # five of a kind
    elif l == 2 and card_count[0][1] == 4:
        t = 2       # four of a kind
    elif card_count[0][1] == 3 and card_count[1][1] == 2:
        t = 3       # full house
    elif card_count[0][1] == 3 and card_count[1][1] == 1:
        t = 4       # three of a kind
    elif card_count[0][1] == 2 and card_count[1][1] == 2:
        t = 5        # two pairs
    elif l == 4 and card_count[0][1] == 2:
        t = 6       # one pair 
    else:
        t = 7       # high card

    return (t, cards, int(bid))

CARD= {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
def get_card_value(card:str) -> int:
    return CARD[card] if card in CARD.keys() else int(card)


CARD_P2= {'T':10, 'J':1, 'Q':12, 'K':13, 'A':14}
def get_card_value_p2(card:str) -> int:
    return CARD_P2[card] if card in CARD_P2.keys() else int(card)

# === Testing suite ===
def get_sinput_path():
    from pathlib import Path
    return Path(__file__).parent.absolute() 

def test_p1():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    hands = sort_by_hand(data)
    w = calculate_winnings(hands)
    assert w == 6440

def test_p2():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    hands = sort_by_hand_p2(data)
    w = calculate_winnings(hands)
    assert w == 5905
