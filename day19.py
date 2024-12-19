#!/usr/bin/env python3

import sys


def dry(pattern, towels, cache):
    if pattern in cache:
        return cache[pattern]

    for towel in towels:
        l = len(towel)
        if pattern[:l] == towel:
            if dry(pattern[l:], towels, cache):
                cache[pattern] = True
                return True
    cache[pattern] = False
    return False


def dry2(pattern, towels, cache, cache2):
    if pattern in cache2:
        return cache2[pattern]

    if not cache.get(pattern, True):
        return 0

    for towel in towels:
        l = len(towel)
        if pattern[:l] == towel:
            res = dry2(pattern[l:], towels, cache, cache2)
            cache2[pattern] = res + cache2.get(pattern, 0)
    return cache2[pattern]


def __main__():
    part1 = 0
    part2 = 0
    cache = {'': True}
    cache2 = {'': 1}
    patterns = []

    with open(sys.argv[1], 'r') as fhan:
        towels = fhan.readline().strip().split(', ')
        fhan.readline()
        for line in fhan.readlines():
            patterns.append(line.strip())

    for pattern in patterns:
        if dry(pattern, towels, cache):
            part1 += 1
            part2 += dry2(pattern, towels, cache, cache2)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == __main__():
    __main__()
