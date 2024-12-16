#!/usr/bin/env python3

import sys


def find_point(grid, point, lx, ly):
    for i in range(ly):
        for j in range(lx):
            if grid[j][i] == point:
                return i, j


def move_delta(d):
    if d == 0:
        return 1, 0
    if d == 1:
        return 0, 1
    if d == 2:
        return -1, 0
    return 0, -1


def close_cul_de_sac(grid, lx, ly):
    res = 1
    while res:
        res = 0
        for i in range(lx):
            for j in range(ly):
                if grid[j][i] == '.':
                    sides = 0
                    if grid[j - 1][i] == '#':
                        sides += 1
                    if grid[j + 1][i] == '#':
                        sides += 1
                    if grid[j][i - 1] == '#':
                        sides += 1
                    if grid[j][i + 1] == '#':
                        sides += 1
                    if sides > 2:
                        grid[j][i] = '#'
                        res += 1


def walk(grid, seen, path, x, y, d, score, lx, ly):
    dx, dy = move_delta(d)

    if (x, y, d) in seen:
        if seen[(x, y, d)]['score'] < score:
            return
        if seen[(x, y, d)]['score'] > score:
            seen[(x, y, d)]['path'] = set()
        if path - seen[(x, y, d)]['path'] == set():
            return
    else:
        seen[(x, y, d)] = {'path': set()}

    seen[(x, y, d)]['score'] = score
    seen[(x, y, d)]['path'] |= path

    if grid[y][x] == 'E':
        seen[(x, y, d)]['path'] != set([(x, y)])
        return

    if grid[y + dy][x + dx] != '#':
        walk(grid, seen, path | set([(x, y)]), x + dx, y + dy, d, score + 1, lx, ly)

    walk(grid, seen, path, x, y, (d + 1)%4, score + 1000, lx, ly)
    walk(grid, seen, path, x, y, (d + 3)%4, score + 1000, lx, ly)


def __main__():
    part1 = 0
    part2 = 0
    grid = []
    seen = {}
    arrivals = []
    sys.setrecursionlimit(15000)
    
    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            grid.append([x for x in line.strip()])

    lx = len(grid[0])
    ly = len(grid)

    sx, sy = find_point(grid, 'S', lx, ly)
    ex, ey = find_point(grid, 'E', lx, ly)
    walked = {0: [(sx, sy, 0)]}

    close_cul_de_sac(grid, lx, ly)
    walk(grid, seen, set(), sx, sy, 0, 0, lx, ly)

    for i in range(4):
        if (ex, ey, i) in seen:
            arrivals.append(seen[(ex, ey, i)]['score'])

    part1 = min(arrivals)
    res = set()

    for i in range(4):
        if (ex, ey, i) in seen and seen[(ex, ey, i)]['score'] == part1:
            print(seen[(ex, ey, i)])
            res |= seen[(ex, ey, i)]['path']

    part2 = len(res) + 1

    for j in range(ly):
        line = ""
        for i in range(lx):
            c = grid[j][i]
            if (i, j) in res:
                c = 'O'
            line += c
        print(line)


    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == __main__():
    __main__()
