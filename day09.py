#!/usr/bin/env python3

import sys


def find_blank(disk, bl, before):
    i = 0
    want = [-1 for _ in range(bl)]
    while i < before:
        if disk[i:i+bl] == want:
            return i
        i += 1
    return -1


def __main__():
    part1 = 0
    part2 = 0
    fileid = 0
    isfile = True
    disk = []
    disk2 = []
    files = []
    
    with open(sys.argv[1], 'r') as fhan:
        line = fhan.readline().strip()

    for x in line:
        if isfile:
            files.append((int(x), len(disk)))
            for i in range(int(x)):
                disk.append(fileid)
            isfile = False
            fileid += 1
        else:
            for i in range(int(x)):
                disk.append(-1)
            isfile = True

    disk2 = list(disk)
    i = 0
    j = len(disk) - 1
    while i < j:
        if disk[i] >= 0:
            i += 1
        elif disk[j] < 0:
            j -= 1
        else:
            disk[i] = disk[j]
            disk[j] = -1
            i += 1
            j -= 1

    for i in range(len(disk)):
        if disk[i] > 0:
            part1 += disk[i] * i
    
    for i in range(fileid - 1, 0, -1):
        fl, fo = files[i]
        j = find_blank(disk2, fl, fo + fl - 1)
        if j > 0:
            for k in range(fl):
                disk2[j + k] = i
                disk2[fo + k] = -1

    for i in range(len(disk2)):
        if disk2[i] > 0:
            part2 += disk2[i] * i

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == __main__():
    __main__()
