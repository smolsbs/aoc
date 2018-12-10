#!/usr/bin/env python3

from collections import defaultdict
import re
from PIL import Image, ImageDraw
from os import chdir, mkdir

def main():
    with open('input', 'r') as fp:
        data = [x for x in fp.readlines()]
    mkdir('img')
    chdir('img')
    p_pos = defaultdict(lambda: [0, 0])
    p_vel = defaultdict(lambda: [0, 0])
    i = 0
    for point in data:
        info = re.search(r"<(.\d{5}), (.\d{5}).*?<(.\d{1}), (.\d{1})", point)
        p_pos[i][0], p_pos[i][1] = int(info.group(1)), int(info.group(2))
        p_vel[i][0], p_vel[i][1] = int(info.group(3)), int(info.group(4))
        i += 1
    
    i = 0
    end = 10700
    while i < end:
        for k in p_pos.keys():
            p_pos[k][0] += p_vel[k][0] 
            p_pos[k][1] += p_vel[k][1]

        i += 1
        if i > 10600:
            print_clouds(p_pos, i)
            
def print_clouds(p_pos, i):
    #part 1 and part 2 together
    #part1 is the image with the points making the text
    #part2 just read the filename, those are the seconds
    
    img = Image.new('1', (300, 300))
    pts = []
    for k, v in p_pos.items():
        x, y = p_pos[k][0], p_pos[k][1]
        pts.append((x, y))
    d = ImageDraw.Draw(img)
    d.point(pts, 8)
    img.save(str(i)+ '.bmp', format='BMP')


if __name__ == '__main__':
    main()