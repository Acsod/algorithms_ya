# https://contest.yandex.ru/contest/22450/run-report/114109942/
# ближайший ноль

from typing import List


def nearest_null(street: List[int]) -> List[int]:
    first = []
    second = [0] * len(street)
    distance = []
    straight_counter = 10**6
    reverse_counter = 10**6
    for i in range(len(street)):
        j = len(street) - 1 - i
        if street[i] == 0:
            straight_counter = 0
        else:
            straight_counter += 1
        first.append(straight_counter)

        if street[j] == 0:
            reverse_counter = 0
        else:
            reverse_counter +=1
        second[j] = reverse_counter

    for i in range(len(street)):
        distance.append(min(first[i], second[i]))
    
    return distance


def read_input() -> List[int]:
    _ = input()
    street = list(map(int, input().split()))
    return street


def main():
    street = read_input()
    distance = nearest_null(street)
    print(' '.join(map(str, distance)))


main()
