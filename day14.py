#!/usr/bin/env python3

import re
import sys


def quadrant(bot, t, lx, ly):
    x = (bot['x'] + bot['dx'] * t) % lx
    y = (bot['y'] + bot['dy'] * t) % ly
    res = 0

    if x == int(lx / 2):
        return 4
    if y == int(ly / 2):
        return 4
    if x > lx / 2:
        res |= 1
    if y > ly / 2:
        res |= 2
    return res


def printmap(bots, t, lx, ly):
    grid = []
    for _ in range(ly):
        grid.append([' '] * lx)
    for bot in bots:
        x = (bot['x'] + bot['dx'] * t) % lx
        y = (bot['y'] + bot['dy'] * t) % ly
        if grid[y][x] == '#':
            return False
        grid[y][x] = '#'
    for line in grid:
        print(''.join(line))
    print('')
    return True


def __main__():
    part1 = 1
    part2 = 0
    pat = re.compile(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)")    
    bots = []
    lx = 101
    ly = 103
    quadrants = [0] * 5

    if sys.argv[1][0] == 's':
        lx = 11
        ly = 7

    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            res = pat.match(line.strip())
            bots.append({
                'x': int(res.group(1)),
                'y': int(res.group(2)),
                'dx': int(res.group(3)),
                'dy': int(res.group(4))
            })

    for bot in bots:
        quadrants[quadrant(bot, 100, lx, ly)] += 1
    for i in range(4):
        part1 *= quadrants[i]

    while True:
        if printmap(bots, part2, lx, ly):
            break
        part2 += 1


    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == __main__():
    __main__()
