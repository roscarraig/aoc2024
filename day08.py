#!/usr/bin/env python3

import math
import sys


def bounded(nx, ny, lx, ly):
    if nx < 0:
        return False
    if ny < 0:
        return False
    if nx >= lx:
        return False
    if ny >= ly:
        return False
    return True


def __main__():
    part1 = 0
    part2 = 0
    grid = []
    ant = {}
    nodes1 = {}
    nodes2 = set()
    
    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            grid.append(line.strip())

    ly = len(grid)
    lx = len(grid[0]) 

    for j in range(ly):
        for i in range(lx):
            c = grid[j][i]
            if c != '.':
                if c in ant:
                    ant[c].append((i, j))
                else:
                    ant[c] = [(i, j)]

    for a in ant:
        n = len(ant[a])
        if n > 1:
            for i in range(n - 1):
                x1, y1 = ant[a][i]
                for j in range(i + 1, n):
                    x2, y2 = ant[a][j]
                    nx = 2 * x1 - x2
                    ny = 2 * y1 - y2
                    if bounded(nx, ny, lx, ly):
                        if (nx, ny) in nodes1:
                            nodes1[(nx, ny)].add(a)
                        else:
                            nodes1[(nx, ny)] = set([a])
                    nx = 2 * x2 - x1
                    ny = 2 * y2 - y1
                    if bounded(nx, ny, lx, ly):
                        if (nx, ny) in nodes1:
                            nodes1[(nx, ny)].add(a)
                        else:
                            nodes1[(nx, ny)] = set([a])
                    dx = x2 - x1
                    dy = y2 - y1
                    gcd = math.gcd(dx, dy)
                    dx /= gcd
                    dy /= gcd
                    tx = x1
                    ty = y1
                    while bounded(tx, ty, lx, ly):
                        nodes2.add((tx, ty))
                        tx -= dx
                        ty -= dy
                    tx = x1 + dx
                    ty = y1 + dy
                    while bounded(tx, ty, lx, ly):
                        nodes2.add((tx, ty))
                        tx += dx
                        ty += dy

    part1 = len(nodes1)
    part2 = len(nodes2)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == __main__():
    __main__()
