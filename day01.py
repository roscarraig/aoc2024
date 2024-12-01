#!/usr/bin/env python3

import sys


def __main__():
    left = []
    right = []
    part1 = 0
    part2 = 0

    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            x, y = line.strip().split('   ')
            left.append(int(x))
            right.append(int(y))

    left.sort()
    right.sort()

    for i in range(len(left)):
        part1 += abs(left[i] - right[i])
        part2 += left[i] * len([x for x in right if x == left[i]])

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == __main__():
    __main__()
