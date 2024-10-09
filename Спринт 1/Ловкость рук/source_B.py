# https://contest.yandex.ru/contest/22450/run-report/114007179/

# Ловкость рук

from typing import List, Tuple
from collections import Counter


def max_vins(k: int, matrix: List[List[int]]) -> int:
    needs_push = Counter(matrix)
    del needs_push[0]
    can_push = k * 2
    vins = sum(list(map(lambda x: x <= can_push, needs_push.values())))
    return vins


def read_input() -> Tuple[int, List[List[int]]]:
    k = int(input())
    n = 4
    matrix = []
    for i in range(n):
        matrix += list(map(int, [x for x in input().replace('.', '0')]))
    return k, matrix


def main():
    k, matrix = read_input()
    vins = max_vins(k, matrix)
    print(vins)


main()
