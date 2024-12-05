#!/usr/bin/env python3

import re
import sys


def validate_update(rules, update):
    nope = set()
    for page in update:
        if page in nope:
            return 0
        if page in rules:
            nope |= rules[page]
    return int(update[len(update) >> 1])


def fix(rules, update):
    for i in range(len(update)):
        if update[i] in rules:
            for item in rules[update[i]]:
                if item in update[i + 1:]:
                    return fix(rules, update[:i] + [item] + [x for x in update[i:] if x != item])
    return int(update[len(update) >> 1])


def __main__():
    part1 = 0
    part2 = 0
    isrules = True
    rules = {}
    updates = []
    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            if isrules:
                if '|' in line:
                    a, b = line.strip().split('|')
                    if b in rules:
                        rules[b].add(a)
                    else:
                        rules[b] = set([a])
                else:
                    isrules = False
            else:
                updates.append(line.strip().split(','))

    for entry in updates:
        v = validate_update(rules, entry)
        if v:
            part1 +=  v
        else:
            part2 += fix(rules, entry)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == __main__():
    __main__()
