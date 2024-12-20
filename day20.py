#!/usr/bin/env python3

import sys


def locate(grid, target):
    ly = len(grid)
    lx = len(grid[0])

    for j in range(1, ly - 1):
        for i in range(1, lx - 1):
            if grid[j][i] == target:
                return i, j

def walk(grid, x, y):
    while True:
        if grid[y - 1][x] == -1:
            grid[y - 1][x] = grid[y][x] + 1
            y -= 1
        elif grid[y + 1][x] == -1:
            grid[y + 1][x] = grid[y][x] + 1
            y += 1
        elif grid[y][x - 1] == -1:
            grid[y][x - 1] = grid[y][x] + 1
            x -= 1
        elif grid[y][x + 1] == -1:
            grid[y][x + 1] = grid[y][x] + 1
            x += 1
        else:
            return


def bypasses(grid, hop, threshold):
    res = 0
    ly = len(grid)
    lx = len(grid[0])

    for j in range(1, ly - 1):
        for i in range(1, lx - 1):
            if grid[j][i] >= 0:
                for b in range(-hop, hop + 1):
                    if b + j < 1 or b + j > ly - 2:
                        continue
                    ar = hop - abs(b)
                    for a in range(-ar, ar + 1):
                        if a + i < 1 or a + i > lx - 2:
                            continue
                        d = abs(a) + abs(b)
                        save =  grid[j + b][i + a] - grid[j][i] - d
                        if save >= threshold:
                            res += 1
    return res


def __main__():
    part1 = 0
    part2 = 0
    grid = []

    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            grid.append(line.strip())

    start = locate(grid, 'S')
    finish = locate(grid, 'E')
    grid2 = [[-2] * len(grid[0]) for _ in range(len(grid))]

    for j in range(1, len(grid) - 1):
        for i in range(1, len(grid[0])):
            if grid[j][i] in ['.', 'S', 'E']:
                grid2[j][i] = -1

    grid2[start[1]][start[0]] = 0
    walk(grid2, start[0], start[1])
    part1 = bypasses(grid2, 2, 100)
    part2 = bypasses(grid2, 20, 100)
    
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == __main__():
    __main__()
