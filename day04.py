#!/usr/bin/env python3

import re
import sys


def scan(grid, y, x, dy, dx):
    for i in range(4):
        if grid[y + dy * i][x + dx * i] != 'XMAS'[i]:
            return False
    return True


def scan2(grid, y, x):
    if grid[y][x] != 'A':
        return False
    if grid[y - 1][x - 1] not in 'MS':
        return False
    if grid[y + 1][x - 1] not in 'MS':
        return False
    if grid[y + 1][x + 1] not in 'MS':
        return False
    if grid[y - 1][x + 1] not in 'MS':
        return False
    if grid[y - 1][x - 1] == grid[y + 1][x + 1]:
        return False
    if grid[y - 1][x + 1] == grid[y + 1][x - 1]:
        return False
    return True


def __main__():
    part1 = 0
    part2 = 0
    grid = []
    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            grid.append(line.strip())

    ly = len(grid)
    lx = len(grid[0]) 
    for j in range(ly):
        for i in range(lx):
            if i < lx - 3 and scan(grid, j, i, 0, 1):
                part1 += 1
            if j < ly - 3 and i < lx - 3 and scan(grid, j, i, 1, 1):
                part1 += 1
            if j < ly - 3 and scan(grid, j, i, 1, 0):
                part1 += 1
            if j < ly - 3 and i > 2 and scan(grid, j, i, 1, -1):
                part1 += 1
            if i > 2 and scan(grid, j, i, 0, -1):
                part1 += 1
            if j > 2 and i > 2 and scan(grid, j, i, -1, -1):
                part1 += 1
            if j > 2 and scan(grid, j, i, -1, 0):
                part1 += 1
            if j > 2 and i < lx - 3 and scan(grid, j, i, -1, 1):
                part1 += 1

    print(lx, ly)
    for j in range(1, ly - 1):
        for i in range(1, lx - 1):
            if scan2(grid, j, i):
                part2 += 1

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == __main__():
    __main__()
