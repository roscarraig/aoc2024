#!/usr/bin/env python3

import sys


def walk(garden, i, j, region, lx, ly):
    plant = garden[(i, j)]['plant']
    perimiter = 0
    edge = 0
    garden[(i, j)]['region'] = region

    if i == 0:
        perimiter += 1
        edge |= 1
    elif garden[(i - 1, j)]['plant'] != plant:
        perimiter += 1
        edge |= 1
    else:
        if garden[(i - 1, j)]['region'] is None:
            walk(garden, i - 1, j, region, lx, ly)

    if j == 0:
        perimiter += 1
        edge |= 2
    elif garden[(i, j - 1)]['plant'] != plant:
        perimiter += 1
        edge |= 2
    else:
        if garden[(i, j - 1)]['region'] is None:
            walk(garden, i, j - 1, region, lx, ly)

    if i == lx - 1:
        perimiter += 1
        edge |= 4
    elif garden[(i + 1, j)]['plant'] != plant:
        perimiter += 1
        edge |= 4
    else:
        if garden[(i + 1, j)]['region'] is None:
            walk(garden, i + 1, j, region, lx, ly)

    if j == ly - 1:
        perimiter += 1
        edge |= 8
    elif garden[(i, j + 1)]['plant'] != plant:
        perimiter += 1
        edge |= 8
    else:
        if garden[(i, j + 1)]['region'] is None:
            walk(garden, i, j + 1, region, lx, ly)

    garden[(i, j)]['perimiter'] = perimiter
    garden[(i, j)]['edge'] = edge


def sidle(garden, i, j, lx, ly):
    e = garden[(i, j)]['edge']
    s = 0

    for f in [1, 4]:
        if e & f:
            if j == ly - 1:
                s += 1
            elif e & 8:
                s += 1
            elif garden[(i, j + 1)]['edge'] & f == 0:
                s += 1

    for f in [2, 8]:
        if e & f:
            if i == ly - 1:
                s += 1
            elif e & 4:
                s += 1
            elif garden[(i + 1, j)]['edge'] & f == 0:
                s += 1

    return s


def __main__():
    part1 = 0
    part2 = 0
    garden = {}
    grid = []
    sides = []
    region = -1
    
    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            grid.append(line.strip())

    lx = len(grid[0])
    ly = len(grid)

    for j in range(ly):
        for i in range(lx):
            garden[(i, j)] = {
                    "plant": grid[j][i],
                    "region": None,
                    "perimiter": 0,
                    "edge": 0
                }

    for j in range(ly):
        for i in range(lx):
            if garden[(i, j)]['region'] is None:
                region += 1
                walk(garden, i, j, region, lx, ly)

    areas = [0] * (region + 1)
    borders = [0] * (region + 1) 
    sides = [0] * (region + 1) 

    for j in range(ly):
        for i in range(lx):
            g = garden[(i, j)]
            areas[g['region']] += 1
            borders[g['region']] += g['perimiter']
            sides[g['region']] += sidle(garden, i, j, lx, ly)

    for i in range(region + 1):
        part1 += areas[i] * borders[i]
        part2 += areas[i] * sides[i]

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == __main__():
    __main__()
