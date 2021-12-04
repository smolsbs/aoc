#!/usr/bin/env python3

from re import findall

def create_boards(data):
    boards = []
    b = {'nums': set(), 'board': [], 'id': None}
    a = []
    i = 0
    for l in data:
        if l != '':
            row = list(map(int, findall(r'\d+', l)))
            a.append(row)
            for j in row:
                b['nums'].add(j)
            b['board'].append(set(row))
        else:
            # make the col sets
            verts = list(zip(a[0], a[1], a[2], a[3], a[4]))
            for j in verts:
                b['board'].append(set(j))
            b['id'] = i
            i += 1
            a = []
            boards.append(b)
            b = {'nums': set(), 'board': []}
            
    return boards

def play_game(boards, nums, squid=False):
    ids = set(range(len(boards)))   # part 2 to keep track of still playing boards
    
    # Loop through all numbers, then through all boards. If n in the set of
    # numbers that make up the board, check which row or col it is in and remove it
    # from said row or col, and also from the set of the unmarked numbers. Then check
    # if the row or col is empty, in which case we have a bingo.
    # For part 2, we only go through the boards still in game, removing them whenever
    # a bingo is achieved until we have our last board that "Bingo's".
    # Return the set of unmarked numbers and the number `n`
    for n in nums:
        for b in boards:
            # for part 1, `b['id'] in ids` will always be True
            if n in b['nums'] and b['id'] in ids:
                b['nums'].remove(n)
                
                for i in range(len(b['board'])):
                    if n in b['board'][i]:
                        b['board'][i].remove(n)

                        # part 1
                        if len(b['board'][i]) == 0 and not squid:
                            return (b['nums'], n)

                        # part 2
                        elif len(b['board'][i]) == 0 and squid:
                            ids.remove(b['id'])
                            if len(ids) == 0:
                                return (b['nums'], n)
                            # just in case we bingo on a row and col at the same time
                            break

def main():
    with open('input', 'r') as fp:
        data = fp.read().split('\n')
    nums = list(map(int, data[0].split(',')))
    boards = create_boards(data[2:])
    
    a, b = play_game(boards, nums)
    p1 = sum(a)*b
    print(f'part 1: {p1}')

    nums = list(map(int,data[0].split(',')))
    boards = create_boards(data[2:])
    c, d = play_game(boards, nums, True)

    p2 = sum(c)*d

    print(f'part 2: {p2}')

if __name__ == '__main__':
    main()