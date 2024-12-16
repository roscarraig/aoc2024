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


def move(grid, x, y, dir):
    nx = x
    ny = y
    
    if dir == '<':
        nx -= 1
    elif dir == '^':
        ny -= 1
    elif dir == '>':
        nx += 1
    elif dir == 'v':
        ny += 1

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


def __main__():
    part1 = 0
    part2 = 0
    grid = []
    ingrid = True
    moves = ''
    
    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            if ingrid:
                if len(line.strip()) > 0:
                    grid.append([x for x in line.strip()])
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

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == __main__():
    __main__()
