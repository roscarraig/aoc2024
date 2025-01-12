#!/usr/bin/env python3

import util
import sys


def day1(lines):
    part1 = 0
    part2 = 0
    left = []
    right = []

    for line in lines:
        x, y = line.strip().split('   ')
        left.append(int(x))
        right.append(int(y))

    left.sort()
    right.sort()

    for i in range(len(left)):
        part1 += abs(left[i] - right[i])
        part2 += left[i] * len([x for x in right if x == left[i]])

    return part1, part2


def __main__():
    if int(sys.argv[1]) in [1]:
        lines = util.read_file_line(sys.argv[2])

    if sys.argv[1] == '1':
        part1, part2 = day1(lines)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == __main__():
    __main__()
