#!/usr/bin/env python3

import aocUtils

def main():
    data = aocUtils.loadInput('input')
    gamma = ''
    epsilon = ''
    oxigen = data[:]
    carbon = data[:]

    for i in range(len(data[0])):
        c_tot = {'0':0, '1':0}
        c_O2 = {'0':0, '1':0}
        c_CO2 = {'0':0, '1':0}
        for v in data:
            c_tot[v[i]] += 1

            # since we're using this for loop going through all nums
            # check if v exists in the oxigen and carbon lists
            # if yes count the i-th digit for each bit criteria
            if v in oxigen:
                c_O2[v[i]] += 1
            if v in carbon:
                c_CO2[v[i]] += 1

        # part 1
        nums = sorted(c_tot, reverse=True, key=c_tot.get)
        gamma += nums[0]
        epsilon += nums[1]

        # part 2
        # get most common bit for oxigen
        m_c = sorted(c_O2, reverse=True, key=c_O2.get)[0]
        if c_O2['0'] == c_O2['1']:
            m_c = '1'

        #  get least common bit for carbon
        l_c = sorted(c_CO2, key=c_CO2.get)[0]
        if c_CO2['0'] == c_CO2['1']:
            l_c = '0'

        # filter numbers that don't obey the bit criteria
        if len(oxigen) != 1:
            oxigen = [x for x in oxigen if x[i] == m_c]
        if len(carbon) != 1:
            carbon = [x for x in carbon if x[i] == l_c]


    p1 = int(gamma, 2) * int(epsilon, 2)
    p2 = int(oxigen[0], 2) * int(carbon[0], 2)

    print(f'part1: {p1}')
    print(f'part2: {p2}')

if __name__ == '__main__':
    main()
