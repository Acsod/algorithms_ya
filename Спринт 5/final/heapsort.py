# Пирамидальная сортировка
# https://contest.yandex.ru/contest/24810/run-report/116204615/

"""
-- Описание --
Написан алгоритм Пирамидальной сортировки heapsort. На вход получаем массив данных, из его элементов создаем невозрастающую кучу с помощью
компоратора. Далее почередно извлекаем из кучи самый приоритетный элемент, поддерживая кучу в состоянии невозрастания. Когда все элементы
извлечены - получаем отсортированный массив.

-- Доказательство --
Передаем в heapsort неотсортированный массив элементов. С помощью heap_add и sift_up (с компоратором) добавляем элементы в конец кучи, каждый
раз, просеивая вверх (чтобы каждый элемент занял свое место по индексу и сохранилось невозрастание). Когда все элементы добавлены, поочередно
вытаскиваем вершину (наиболее приоритетный, в нашем случае, элемент) в отдельный массив и выполняем просеивание вниз, чтобы актуализировать
состояние невозрастающей кучи для оставшихся элементов. Когда элементы в куче закончились - возвращаем отсортированный массив.

-- Временная сложность --
Выделение массива под кучу работает за О(1)
Добавление элементов в кучу работает за О(log(x)) для каждого добавленного элемента, где n - число элементов в массиве, а x принимает значения
от 1 до n. В общей сложности, можем считать, что создание просеянной кучи занимает O(n * log(n)).
Удаление самого приоритетного элемента занимает O(1) * n на само удаление элементов и также O(n * log(n)) для актуализации кучи (просеивания
вниз). Итого можем считать, что алгоритм работает за 2 * O(n * log(n)) или за O(n * log(n)).

-- Пространственная сложность --
Для хранения исходного массива у нас О(n). Для хранения кучи также выделяем О(n). И для хранения отсортированного массива О(n). Итого 3 * О(n)
или просто О(n).

"""


from typing import List, Tuple


# Компоратор
def comporator(x_1: List, x_2: List, compare: str='less'):
    if compare == 'more':
        if x_1[1] != x_2[1]:
            return x_1[1] > x_2[1]
        elif x_1[2] != x_2[2]:
            return x_1[2] < x_2[2]
        else:
            return x_1[0] < x_2[0]
    elif compare == 'less':
        if x_1[1] != x_2[1]:
            return x_1[1] < x_2[1]
        elif x_1[2] != x_2[2]:
            return x_1[2] > x_2[2]
        else:
            return x_1[0] > x_2[0]
    else:
        raise ValueError("Choose compare as 'less' or 'more'") 


# Просеивание вверх
def sift_up(heap: List, idx: int) -> None:
    # если пришли в вершину - выходим
    if idx == 1:
        return
    
    # ищем родителя
    par_idx = idx // 2

    # если ребенок больше родителя - меняем их местами
    if comporator(heap[idx], heap[par_idx], compare='more'):
        heap[idx], heap[par_idx] = heap[par_idx], heap[idx]
        sift_up(heap, par_idx)

    return


# Просеивание вниз
def sift_down(heap: List, idx: int) -> None:

    heap_max_index = len(heap) - 1
    left = idx * 2
    right = idx * 2 + 1

    # если нет детей, выходим из функции
    if left > heap_max_index:
        return    
    
    # если есть дети, ищем наибольший элемент их них
    if right <= heap_max_index and comporator(heap[right], heap[left], compare='more'):
        index_largest = right
    else:
        index_largest = left

    # сравниваем текущий элемент с наибольшим ребенком
    if comporator(heap[index_largest], heap[idx], compare='more'):
        heap[index_largest], heap[idx] = heap[idx], heap[index_largest]
        sift_down(heap, index_largest)

    return 


# Функция для добавления элемента в кучу
def heap_add(heap: List, key: int) -> None:
    # добавляем элемент в конец кучи и просееваем
    heap.append(key)
    index = len(heap)-1
    sift_up(heap, index)


# Функция для извлечения самого приоритетного элемента
def pop_max(heap: List) -> List:
    # сохраняем вершину, замещаем ее последним элементом и просеесваем
    res = heap[1]
    heap[1] = heap[-1]
    heap.pop()
    sift_down(heap, 1)
    return res

   
# Функция сортировки
def heapsort(persons: List) -> List:
    # создаем пустую кучу
    heap = [None]

    # вставляем в неё элементы массива
    for item in persons:
        heap_add(heap, item)

    # извлекаем самые приоритетные элементы по очереди
    persons_sorted = []
    while len(heap) > 1:
        max_item = pop_max(heap) 
        persons_sorted.append(max_item)

    return persons_sorted 


# Фунция для чтения данных
def read_input() -> Tuple[int, List]:
    n = int(input())
    persons = []
    for i in range(n):
        person = input().split()
        person[1], person[2] = int(person[1]), int(person[2])
        persons.append(person)
    return n, persons


def main():
    n, persons = read_input()
    persons_sorted = heapsort(persons)
    answer = [x[0] for x in persons_sorted]
    print(*answer, sep='\n')


main()
