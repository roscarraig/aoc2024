#!/usr/bin/env python3

import sys


def walk(grid, x, y, lx, ly, part):
    if part == 1:
        result = set()
    else:
        result = 0

    e = grid[y][x]

    if e == 9:
        if part == 1:
            return set([(x, y)])
        return 1

    if x > 0 and grid[y][x - 1] == e + 1:
        if part == 1:
            result |= walk(grid, x - 1, y, lx, ly, part)
        else:
            result += walk(grid, x - 1, y, lx, ly, part)
    if x < lx - 1 and grid[y][x + 1] == e + 1:
        if part == 1:
            result |= walk(grid, x + 1, y, lx, ly, part)
        else:
            result += walk(grid, x + 1, y, lx, ly, part)
    if y > 0 and grid[y - 1][x] == e + 1:
        if part == 1:
            result |= walk(grid, x, y - 1, lx, ly, part)
        else:
            result += walk(grid, x, y - 1, lx, ly, part)
    if y < ly - 1 and grid[y + 1][x] == e + 1:
        if part == 1:
            result |= walk(grid, x, y + 1, lx, ly, part)
        else:
            result += walk(grid, x, y + 1, lx, ly, part)
    return result


def __main__():
    part1 = 0
    part2 = 0
    grid = []
    
    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            grid.append([int(x) for x in line.strip()])

    ly = len(grid)
    lx = len(grid[0]) 

    for j in range(ly):
        for i in range(lx):
            if grid[j][i] == 0:
                res = walk(grid, i, j, lx, ly, 1)
                part1 += len(res)
                part2 += walk(grid, i, j, lx, ly, 2)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == __main__():
    __main__()
