from collections import deque, defaultdict

def main(n_player, last_num):
    circle = deque([0])
    pid = 1
    players = defaultdict(lambda: 0)

    for i in range(1, last_num + 1):
        if i%23 == 0:
            players[pid] += i
            circle.rotate(7)
            players[pid] += circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(i)
        pid = (pid + 1) % n_player
    print(max(players.values()))

with open('input', 'r') as fp:
    data = fp.read().split(' ')
    main(int(data[0]), int(data[6]))
    main(int(data[0]), 100 * int(data[6]))