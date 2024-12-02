#!/usr/bin/env python3

import sys


def check_report(report):
    if report[0] == report[1]:
        return False
    if report[1] > report[0]:
        trend = 1
    else:
        trend = -1

    for i in range(len(report) - 1):
        diff = (report[i + 1] - report[i]) * trend
        if diff < 1:
            return False
        if diff > 3:
            return False
    return True


def check_damped_report(report):
    for i in range(len(report)):
        report1 = list(report)
        del report1[i]
        if check_report(report1):
            return True
    return False


def __main__():
    part1 = 0
    part2 = 0

    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            report = [int(x) for x in line.strip().split(' ')]
            if check_report(report):
                part1 += 1
                part2 += 1
            elif check_damped_report(report):
                part2 += 1


    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == __main__():
    __main__()
