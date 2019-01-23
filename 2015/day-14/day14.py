#!/usr/bin/python
from collections import defaultdict

def main():
    seconds = 2503
    # Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
    reindeers = defaultdict()
    with open('input', 'r') as fp:
        for x in fp.read().strip().split('\n'):
            x = x.split(' ')
            reindeers[x[0]] = {"speed": int(x[3]),
                                "fly": int(x[6]),
                                "rest": int(x[13]),
                                "change": int(x[6]),
                                "distance": 0,
                                "pts": 0}

    is_flying = list(reindeers.keys())
    for s in range(seconds):
        for k, v in reindeers.items():
            if k in is_flying:
                v['distance'] += v['speed']
                if s > v["change"]:
                    is_flying.pop(is_flying.index(k))
                    v["change"] += v["rest"]

            else:
                if s > v["change"]:
                    is_flying.append(k)
                    v["change"] += v["fly"]
        # broken smh
        # a = []
        # for k, v in sorted(reindeers.items(), key=lambda x: x[1]['distance'], reverse=True):
        #     a.append((k, v['distance']))
        # reindeers[a[0][0]]['pts'] += 1

    print("sorting for distance...")
    for k, v in sorted(reindeers.items(), key=lambda x: x[1]['distance'], reverse=True):
        print("{}: {}".format(k, v['distance']))

    # print("sorting for points...")
    # for k, v in sorted(reindeers.items(), key=lambda x: x[1]['pts'], reverse=True):
    #     print("{}: {}".format(k, v['pts']))

if __name__ == '__main__':
    main()