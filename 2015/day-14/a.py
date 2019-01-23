import re
import itertools
import collections

text = open('input').read()
regex = r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.'
history = collections.defaultdict(list)
for who, speed, duration, rest in re.findall(regex, text):
    steps = itertools.cycle([int(speed)]*int(duration) + [0]*int(rest))
    history[who] = list(itertools.accumulate(next(steps) for _ in range(2503)))

by_dist = max(h[-1] for h in history.values())
print(by_dist)

scored = [i for a in zip(*history.values()) for i, v in enumerate(a) if v==max(a)]
by_points = max(collections.Counter(scored).values())
print(by_points)