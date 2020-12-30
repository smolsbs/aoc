#!/usr/bin/env python3

from re import findall

HEIGHT_VALS = {'in': [59, 76], 'cm': [150, 193]}

# https://stackoverflow.com/questions/54372218/how-to-split-a-list-into-sublists-based-on-a-separator-similar-to-str-split
def split(sequence, sep):
    chuck = []
    for val in sequence:
        if val == sep:
            yield chuck
            chuck = []
        else:
            chuck.append(val)
    yield chuck

def check_if_valid_passport(p):
    
    try:
        int(p['hcl'][1:], 16)
        int(p['pid'])
        hgt, t = findall(r'(\d{2,3})(\w{2})', p['hgt'])[0]
    except:
        return 0
    if p['hcl'][0] != '#' or len(p['hcl']) != 7:
        return 0
    if len(p['byr']) != 4 or int(p['byr']) < 1920 or int(p['byr']) > 2002:
        return 0
    if len(p['iyr']) != 4 or int(p['iyr']) < 2010 or int(p['iyr']) > 2020:
        return 0
    if len(p['eyr']) != 4 or int(p['eyr']) < 2020 or int(p['eyr']) > 2030:
        return 0
    if p['ecl'] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
        return 0
    if len(p['pid']) != 9:
        return 0    
    if int(hgt) < HEIGHT_VALS[t][0] or int(hgt) > HEIGHT_VALS[t][1]:
        return 0
    return 1

def main():
    with open('input', 'r') as fp:
        data = [x for x in fp.readlines()]
    valid_users = 0
    really_valid_users = 0
    for person in split(data, '\n'):
        fields = ' '.join([x.strip() for x in person]).split(' ')
        passport = dict()
        for j in fields:
            k, v = j.split(':')
            passport[k] = v

        if len(passport.keys()) == 8 or (len(passport.keys()) == 7 and 'cid' not in passport.keys()):
            really_valid_users += check_if_valid_passport(passport)
            valid_users += 1
            

    print('part 1: {:d}'.format(valid_users))
    print('part 2: {:d}'.format(really_valid_users))

if __name__ == '__main__':
    main()