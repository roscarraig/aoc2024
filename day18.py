#!/usr/bin/env python3

import sys


def print_map(rocks, seen, i, w):
    result = []
    for y in range(w):
        line = ''
        for x in range(w):
            if rocks[y][x] <= i:
                line += '#'
            elif (x, y) in seen:
                line += '@'
            else:
                line += '.'
        result.append(line)
    return result


def __main__():
    part1 = 0
    part2 = 0
    w = 71
    if sys.argv[1][0] == 's':
        w = 7
    grid = [[-1] * w for _ in range(w)]
    rocks = [[1000000000] * w for _ in range(w)]
    rockl = []
    wave = set([(0, 0)])
    seen = set()
    neww = set()
    i = 0
    j = 0

    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            x, y = [int(a) for a in line.strip().split(',')]
            rocks[y][x] = i
            rockl.append((x, y))
            j += 1
            if j >= 1024 or w == 7:
                i += 1

    i = 0
    while (w - 1, w -1) not in wave:
        i += 1
        for x, y in wave:
            if x > 0 and rocks[y][x - 1] > i and (x - 1, y) not in seen:
                neww.add((x - 1, y))
            if x < w - 1 and rocks[y][x + 1] > i and (x + 1, y) not in seen:
                neww.add((x + 1, y))
            if y > 0 and rocks[y - 1][x] > i and (x, y - 1) not in seen:
                neww.add((x, y - 1))
            if y < w - 1 and rocks[y + 1][x] > i and (x, y + 1) not in seen:
                neww.add((x, y + 1))
        seen |= wave
        wave = neww
        neww = set()

    part1 = i

    wave = set([(0, 0)])
    seen = set()
    while len(wave) > 0:
        neww = set()
        if (w - 1, w - 1) in wave:
            last = print_map(rocks, seen, i, w)
            i += 1
            wave = set([(0, 0)])
            seen = set()
            continue
        for x, y in wave:
            if x > 0 and rocks[y][x - 1] > i and (x - 1, y) not in seen:
                neww.add((x - 1, y))
            if x < w - 1 and rocks[y][x + 1] > i and (x + 1, y) not in seen:
                neww.add((x + 1, y))
            if y > 0 and rocks[y - 1][x] > i and (x, y - 1) not in seen:
                neww.add((x, y - 1))
            if y < w - 1 and rocks[y + 1][x] > i and (x, y + 1) not in seen:
                neww.add((x, y + 1))
        seen |= wave
        wave = neww

    this = print_map(rocks, seen, i, w)
    for j in range(w):
        for i in range(w):
            if this[j][i] == '#' and last[j][i] != '#':
                part2 = f"{i},{j}"

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == __main__():
    __main__()
