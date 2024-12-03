#!/usr/bin/env python3

import re
import sys


def __main__():
    enabled = True
    part1 = 0
    part2 = 0
    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            for op in re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', line.strip()):
                if op[0:2] == 'do':
                    if op == 'do()':
                        enabled = True
                    else:
                        enabled = False
                else:
                    vals = op[4:-1].split(',')
                    part1 += int(vals[0]) * int(vals[1])
                    if enabled:
                        part2 += int(vals[0]) * int(vals[1])
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == __main__():
    __main__()
