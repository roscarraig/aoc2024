#!/usr/bin/env python3

import sys


def translate(x):
    if x == 0:
        return [1]
    if len(str(x)) % 2 == 0:
        l = int(len(str(x)) / 2)
        return [int(str(x)[0:l]), int(str(x)[l:])]
    return [int(x) * 2024]


def __main__():
    part1 = 0
    part2 = 0
    stones = {}
    
    with open(sys.argv[1], 'r') as fhan:
        for x in fhan.readline().strip().split(' '):
            if x not in stones:
                stones[int(x)] = [0, 0]
            stones[int(x)][0] += 1

    for i in range(75):
        l = len(stones)

        for x in list(stones):
            stones[x][(i + 1) % 2] = 0

        for x in list(stones):
            if stones[x][i % 2] > 0:
                for y in translate(x):
                    if y not in stones:
                        stones[y] = [0, 0]
                    stones[y][(i + 1) % 2] += stones[x][i % 2]

        if i == 25:
            for x in stones:
                part1 += stones[x][1]

    for x in stones:
        part2 += stones[x][1]

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == __main__():
    __main__()
