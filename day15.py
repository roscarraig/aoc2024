#!/usr/bin/env python3

import sys


def findbot(grid, lx, ly):
    for j in range(ly):
        for i in range(lx):
            if grid[j][i] == '@':
                return (i, j)


def print_map(grid):
    for j in range(len(grid)):
        print(''.join(grid[j]))


def dirdelta(dir):
    nx = 0
    ny = 0
    
    if dir == '<':
        nx = -1
    elif dir == '^':
        ny = -1
    elif dir == '>':
        nx = 1
    elif dir == 'v':
        ny = 1
    return nx, ny

def move(grid, x, y, dir):
    nx, ny = dirdelta(dir)

    if grid[ny][nx] == '.':
        grid[ny][nx] = grid[y][x]
        grid[y][x] = '.'
        return True, nx, ny
    elif grid[ny][nx] == '#':
        return False, x, y
    elif grid[ny][nx] == 'O':
        change, _, _ =  move(grid, nx, ny, dir)
        if change:
            grid[ny][nx] = grid[y][x]
            grid[y][x] = '.'
            return True, nx, ny
        return False, x, y


def boxval(grid, lx, ly):
    result = 0

    for j in range(ly):
        for i in range(lx):
            if grid[j][i] == 'O':
                result += 100 * j + i
    return result


def canmove(grid, x, y, dir):
    dx, dy = dirdelta(dir)
    nx = x + dx
    ny = y + dy

    if grid[ny][nx] == '.':
        return True
    if grid[ny][nx] == '#':
        return False
    if ny == 0:
        return canmove(grid, nx + 2*x, y, dir)
    if grid[ny][nx] == '.' and grid[y][x] == '@':
        return True
    if grid[y][x] == '@':
        if grid[ny][nx] == '[':
            return canmove(grid, nx, ny, dir)
        return canmove(grid, nx - 1, ny, dir)
    if '#' in [grid[ny][nx], grid[ny][nx + 1]]:
        return False
    if grid[ny][nx] == '.':
        if grid[ny][nx + 1] == '.':
            return True
        return c, anmove(grid, nx + 1, ny, dir)
    if grid[ny][nx] == '[':
        return canmove(grid, nx. ny. dir)
    if not canmove(grid, nx - 1, ny, dir):
        return False
    if grid[ny][nx + 1] == '.':
        return True
    return canmove(grid, nx + 1, ny, dir)


def __main__():
    part1 = 0
    part2 = 0
    grid = []
    grid2 = []
    ingrid = True
    moves = ''
    
    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            if ingrid:
                if len(line.strip()) > 0:
                    grid.append([x for x in line.strip()])
                    nline = []
                    for x in line.strip():
                        if x == 'O':
                            nline.append('[')
                            nline.append(']')
                        elif x == '@':
                            nline.append(x)
                            nline.append('.')
                        else:
                            nline.append(x)
                            nline.append(x)
                    grid2.append(nline)

                else:
                    ingrid = False
            else:
                moves += line.strip()

    lx = len(grid[0])
    ly = len(grid)
    x, y = findbot(grid, lx, ly)

    for m in moves:
        _, x, y = move(grid, x, y, m)

    part1 = boxval(grid, lx, ly)

    x, y = findbot(grid2, lx, ly)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == __main__():
    __main__()
