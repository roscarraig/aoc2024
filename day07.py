#!/usr/bin/env python3

import sys


def trial(target, vals, part2):
    if len(vals) == 2:
        if vals[0] + vals[1] == target:
            return True
        if vals[0] * vals[1] == target:
            return True
        if part2 and target == int(str(vals[0]) + str(vals[1])):
            return True
        return False

    if len(vals) == 1:
        if vals[0] == target:
            return True
        return False

    if trial(target, [vals[0] + vals[1]] + vals[2:], part2):
        return True
    if trial(target, [vals[0] * vals[1]] + vals[2:], part2):
        return True
    if part2 and trial(target, [int(str(vals[0]) + str(vals[1]))] + vals[2:], part2):
        return True
    return False


def __main__():
    part1 = 0
    part2 = 0
    
    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            vals = [int(x) for x in line.strip().replace(':', '').split(' ')]
            if trial(vals[0], vals[1:], False):
                part1 += vals[0]
                part2 += vals[0]
            elif trial(vals[0], vals[1:], True):
                part2 += vals[0]

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == __main__():
    __main__()
