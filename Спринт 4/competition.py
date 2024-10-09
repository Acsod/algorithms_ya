# Соревнование
# Жители Алгосов любят устраивать турниры по спортивному программированию. Все участники
# разбиваются на пары и соревнуются друг с другом. А потом два самых сильных программиста
# встречаются в финальной схватке, которая состоит из нескольких раундов. Если в очередном
# раунде выигрывает первый участник, в таблицу с результатами записывается 0, если второй, 
# то 1. Ничьей в раунде быть не может.
# Нужно определить наибольший по длине непрерывный отрезок раундов, по результатам которого 
# суммарно получается ничья. Например, если дана последовательность 0 0 1 0 1 1 1 0 0 0, то 
# раунды с 2-го по 9-й (нумерация начинается с единицы) дают ничью.


from typing import List, Tuple


def faiting(raunds: List) -> List:
    answer = 0
    sum_now = 0
    pref_sum = []

    # префексные суммы
    for i in raunds:
        if i == 1:
            sum_now += 1
        else:
            sum_now -= 1
        pref_sum.append(sum_now)

    # собираем интервалы с равными значениями
    starts_sum = {0: [-1, 0]}  # изначально ничья
    for i in range(len(pref_sum)):
        if pref_sum[i] not in starts_sum:
            starts_sum[pref_sum[i]] = [i, i]
        else:
            starts_sum[pref_sum[i]][1] = i

        # сохраняем наибольший
        interval = starts_sum[pref_sum[i]][1] - starts_sum[pref_sum[i]][0]
        if interval > answer:
            answer = interval    

    return answer


def read_input() -> Tuple[str, List]:
    n = int(input())
    raunds = list(map(int, input().split()))
    return n, raunds


def main():
    n, raunds = read_input()
    print(faiting(raunds))


main()
