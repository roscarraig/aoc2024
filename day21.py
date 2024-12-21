#!/usr/bin/env python3

import sys


def path1(start, finish):
    rows = {
            "0": 0, "A": 0,
            "1": 1, "2": 1, "3": 1,
            "4": 2, "5": 2, "6": 2,
            "7": 3, "8": 3, "9": 3
    }
    cols = {
            "0": 1, "A": 2,
            "1": 0, "2": 1, "3": 2,
            "4": 0, "5": 1, "6": 2,
            "7": 0, "8": 1, "9": 2
    }
    result = ''
    if rows[start] == 0 and cols[finish] == 0:
        result += '^' * (rows[finish] - rows[start])
        result += '<' * (cols[start] - cols[finish])
    elif cols[start] == 0 and rows[finish] == 0:
        result += '>' * (cols[finish] - cols[start])
        result += 'v' * (rows[start] - rows[finish])
    else: 
        result += '<' * (cols[start] - cols[finish])
        result += 'v' * (rows[start] - rows[finish])
        result += '^' * (rows[finish] - rows[start])
        result += '>' * (cols[finish] - cols[start])
    result += 'A'
    return result


def path2(start, finish):
    rows = {
        "<": 0, "v": 0, ">": 0,
        "^": 1, "A": 1
    }
    cols = {
        "<": 0, "^": 1, "v": 1, "A": 2, ">": 2
    }
    result = '>' * (cols[finish] - cols[start])
    result += '^' * (rows[finish] - rows[start])
    result += '<' * (cols[start] - cols[finish])
    result += 'v' * (rows[start] - rows[finish])
    result += 'A'
    return result


def path1code(code):
    result = ''

    for i in range(len(code) - 1):
        result += path1(code[i], code[i + 1])
    return result


def path2code(code):
    result = ''

    for i in range(len(code) - 1):
        result += path2(code[i], code[i + 1])
    return result

def rpath2code(code, depth, caches):
    if code in caches[depth]:
        return caches[depth][code]

    layer = path2code('A' + code)
    res = ''

    if depth == 1:
        return layer

    for x in layer[:len(layer) - 1].split('A'):
        res += rpath2code(x + 'A', depth - 1, caches)
    caches[depth][code] = res
    return res


def __main__():
    part1 = 0
    part2 = 0
    grid = []
    paths = {}
    codes = []
    cache = {}
    caches = [{}] * 50

    with open(sys.argv[1], 'r') as fhan:
        for line in fhan.readlines():
            codes.append(line.strip())

    for code in codes:
        code1 = path1code('A' + code)
        # code2 = path2code('A' + code1)
        # code3 = path2code('A' + code2)
        code3 = path2code('A' + path2code('A' + code1))
        print(code, len(code3))
        part1 += len(code3) * int(code[:len(code) - 1])

    print(f"Part 1: {part1}")

    for code in codes:
        ncode = path1code('A' + code)
        # print(code, len(rpath2code(ncode, 24, caches)))
        c = rpath2code(ncode, int(sys.argv[2]), caches)
        r = len(c)
        print(code, r, c)
        part2 += r * int(code[:len(code) - 1])
        for j in range(int(sys.argv[2])):
            res = ''
            for x in ncode[:len(ncode) - 1].split('A'):
                res += path2code('A' + x + 'A')
            ncode = res
        print(code, len(ncode), ncode)

    # 2201262916 low
    print(f"Part 2: {part2}")


if __name__ == __main__():
    __main__()
