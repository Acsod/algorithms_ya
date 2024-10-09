# Два велосипеда
# Вася решил накопить денег на два одинаковых велосипеда — себе и сестре. У Васи есть копилка, 
# в которую каждый день он может добавлять деньги (если, конечно, у него есть такая финансовая 
# возможность). В процессе накопления Вася не вынимает деньги из копилки.
# У вас есть информация о росте Васиных накоплений — сколько у Васи в копилке было денег в каждый из дней.
# Ваша задача — по заданной стоимости велосипеда определить:
#   - первый день, в которой Вася смог бы купить один велосипед,
#   - первый день, в который Вася смог бы купить два велосипеда.
# Подсказка: решение должно работать за O(log n).


from typing import List, Tuple


def search_days(cost, series, left, right):
    if left >= right:
        return -2
    middle = (left + right) // 2
    if series[middle] >= cost:
        early = search_days(cost, series, left, middle)
        if early == -2:
            return middle
        else:
            return early
    elif series[middle] < cost:
        return search_days(cost, series, middle + 1, right)
    

def read_input() -> Tuple[int, int, List]:
    n = int(input())
    series = list(map(int, input().split()))
    cost = int(input())
    return n, cost, series


def main():
    n, cost, series = read_input()
    left = 0
    right = n
    answer_1 = search_days(cost, series, left, right)
    answer_2 = search_days(cost * 2, series, left, right)
    print(answer_1 + 1, answer_2 + 1)


main()
