#!/usr/bin/env python3

import sys


def run(box, a):
    p = 0
    r = []
    b = box['b']
    c = box['c']
    box['r'] = []
    while p < box['l']:
        v = box['p'][p + 1]
        i = box['p'][p]
        p += 2
        w = v
        if w == 4:
            w = a
        elif w == 5:
            w = b
        elif w == 6:
            w = c
        if i == 0:
            a = int(a / (1 << w))
        elif i == 1:
            b ^= v
        elif i == 2:
            b = w % 8
        elif i == 3:
            if a != 0:
                p = v
        elif i == 4:
            b ^= c
        elif i == 5:
            r.append(w % 8)
        elif i == 6:
            b = int(a / (1 << w))
        elif i == 7:
            c = int(a / (1 << w))
    return r


def __main__():
    part1 = 0
    part2 = 0
    box = {}
    
    with open(sys.argv[1], 'r') as fhan:
        box['a'] = int(fhan.readline().strip().split(": ")[1])
        box['b'] = int(fhan.readline().strip().split(": ")[1])
        box['c'] = int(fhan.readline().strip().split(": ")[1])
        fhan.readline()
        box['p'] = [int(x) for x in fhan.readline().strip().split(": ")[1].split(',')]
        box['l'] = len(box['p'])

    r = run(box, box['a'])
    part1 = ','.join([str(x) for x in r])
    print(f"Part 1: {part1}")

    for j in range(len(box['p'])):
        for i in range(8):
            r = run(box, (part2 << 3) + i)
            if r[-j - 1] == box['p'][-j - 1]:
                part2 *= 8
                part2 += i
                break
    print(f"Part 2: {part2}")


if __name__ == __main__():
    __main__()
