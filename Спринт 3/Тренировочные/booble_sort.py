# Пузырек
# Чтобы выбрать самый лучший алгоритм для решения задачи, Гоша продолжил изучать разные сортировки. 
# На очереди сортировка пузырьком — https://ru.wikipedia.org/wiki/Сортировка_пузырьком
# Её алгоритм следующий (сортируем по неубыванию):
#   1. На каждой итерации проходим по массиву, поочередно сравнивая пары соседних элементов. Если элемент
#   на позиции i больше элемента на позиции i + 1, меняем их местами. После первой итерации самый большой
#   элемент всплывёт в конце массива.
#   2. Проходим по массиву, выполняя указанные действия до тех пор, пока на очередной итерации не окажется, 
#   что обмены больше не нужны, то есть массив уже отсортирован.
#   3. После не более чем n – 1 итераций выполнение алгоритма заканчивается, так как на каждой итерации хотя
#   бы один элемент оказывается на правильной позиции.
# Помогите Гоше написать код алгоритма.


from typing import List, Tuple

def booble_sort(n, series):
    a = None
    count = 1
    answer = []
    while count != 0:
        count = 0
        for i in range(n-1):
            if series[i] > series[i+1]:
                a = series[i+1]
                series[i+1] = series[i]
                series[i] = a
                count += 1
        tmp = ' '.join(map(str, series))
        if tmp not in answer:
            answer.append(tmp)
    return answer
    

def read_input() -> Tuple[int, List]:
    n = int(input())
    series = list(map(int, input().split()))
    return n, series


def main():
    n, series = read_input()
    print(*booble_sort(n, series), sep='\n')


main()
