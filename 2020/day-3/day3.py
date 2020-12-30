#!/usr/bin/env python3

def ride_down(slope_map, slope_conf):
    """Iterate over the map to get the tree count of a predetermined
    toboggan configuration.

    Args:
        slope_map (list ): map of the slope
        slope_conf (tuple): right (index 0) and down (index 1) values for the slope

    Returns:
        int: number of trees crossing the path"""

    max_right = len(slope_map[0])
    max_down = len(slope_map)
    # px is the lateral position, py is the vertical position
    px, py = (0,0)
    trees = 0


    # interate until we reach the end of the map
    while py < max_down:
        if slope_map[py][px] == '#':
            trees += 1
        px = (px + slope_conf[0]) % max_right # right, making sure to keep it in bounds
        py += slope_conf[1] # down

    return trees

def main():
    with open('input', 'r') as fp:
        data = [[c for c in x.strip()] for x in fp.read().split('\n')]

    slopes = {(1,1), (3,1), (5,1), (7,1), (1,2)}
    p2 = 1

    # get every tree count for each slope config and multiply them together
    for v in slopes:
        t = ride_down(data, v)
        print("({},{}): {}".format(v[0], v[1], t))
        p2 *= t

    print('all multiplied: %d' % p2)

if __name__ == '__main__':
    main()
