#!/usr/bin/env python3

import sys


def find_guard(grid, lx, ly):
    for j in range(ly):
        for i in range(lx):
            if grid[j][i] == '^':
                return(i, j)


def looper(grid, lx, ly, gx, gy, ox, oy):
    if grid[oy][ox] in ['#', '^']:
        return False
    dir = 0
    walk = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    seen = set()

    while (gx, gy, dir) not in seen:
        if gx < 0 or gx >= lx or gy < 0 or gy >= ly:
            return False

        seen.add((gx, gy, dir))
        tx = gx + walk[dir][0]
        ty = gy + walk[dir][1]
        if tx >= 0 and tx < lx and ty >= 0 and ty < ly and (grid[ty][tx] == '#' or (tx == ox and ty == oy)):
            dir += 1
            dir %= 4
        else:
            gx = tx
            gy = ty
    return True


def __main__():
    part1 = set()
    part2 = 0
    grid = []
    walk = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    dir = 0
    
    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            grid.append(line.strip())

    ly = len(grid)
    lx = len(grid[0]) 

    gx, gy = find_guard(grid, lx, ly)
    while gx >= 0 and gx < lx and gy >= 0 and gy < ly:
        part1.add((gx, gy))
        tx = gx + walk[dir][0]
        ty = gy + walk[dir][1]
        if tx >= 0 and tx < lx and ty >= 0 and ty < ly and grid[ty][tx] == '#':
            dir += 1
            dir %= 4
        else:
            gx = tx
            gy = ty

    print(f"Part 1: {len(part1)}")

    gx, gy = find_guard(grid, lx, ly)

    for i in range(lx):
        for j in range(ly):
            if looper(grid, lx, ly, gx, gy, i, j):
                part2 += 1

    print(f"Part 2: {part2}")


if __name__ == __main__():
    __main__()
