
from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product

from helpers import distance, distance_sq, grouped_lines, ints, manhattan, neighs, neighs_bounded


def solve(program):
    run = set()
    acc = 0
    pos = 0

    while pos not in run:
        inst, val = program[pos]
        run.add(pos)

        if inst == 'acc':
            acc += val
            pos += 1
        elif inst == 'jmp':
            pos += val
        elif inst == 'nop':
            pos += 1

    return acc

if __name__ == '__main__':
    lines = []

    with open('8.txt') as f:
        for line in f.readlines():
            sp = line.split()
            lines.append((sp[0], int(sp[1])))

    print(solve(lines))
