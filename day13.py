#!/usr/bin/env python3

import re
import sys


def solve(game, offset = 0):
    px = game['px'] + offset
    py = game['py'] + offset
    ax = game['Ax']
    ay = game['Ay']
    bx = game['Bx']
    by = game['By']

    if (ax*py - ay*px) % (ax * by - ay * bx) == 0:
        j  = int((ax*py - ay*px) / (ax * by - ay * bx))
        if (px - j *bx) % ax == 0:
            i = int((px - j *bx) / ax)
            return 3 * i + j
    return 0


def __main__():
    part1 = 0
    part2 = 0
    games = []
    bpat = re.compile(r'Button (A|B): X\+(\d+), Y\+(\d+)')
    ppat = re.compile(r'Prize: X=(\d+), Y=(\d+)')

    with open(sys.argv[1], 'r') as fhan:
        line = fhan.readline().strip()

        while line:
            game = {}
            res = bpat.match(line)
            game[res.group(1)+'x'] = int(res.group(2))
            game[res.group(1)+'y'] = int(res.group(3))
            line = fhan.readline().strip()
            res = bpat.match(line)
            game[res.group(1)+'x'] = int(res.group(2))
            game[res.group(1)+'y'] = int(res.group(3))
            line = fhan.readline().strip()
            res = ppat.match(line)
            game['px'] = int(res.group(1))
            game['py'] = int(res.group(2))
            games.append(game)
            line = fhan.readline().strip()
            line = fhan.readline().strip()
            part1 += solve(game)
            part2 += solve(game, 10000000000000)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == __main__():
    __main__()
