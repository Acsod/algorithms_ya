# A. Дорогая сеть
# https://contest.yandex.ru/contest/25070/run-report/116690777/

"""
-- Описание --
Необходимо составить остовное дерево из ребер с максимальным весом. Для этого используем кучу библиотеки heapq
с заменой веса на его отрицательное значение, т.к. по умолчанию данная куча на минимум. Т.к. мы состаляем остов
только если имеем одну компоненту связанности, то в остов нужно добавить все вершины. Начиная с произвольной вершины
поочередно добавляем в кучу все смежные вершины. Удаялем вершину из списка необработанных. Затем из кучи извлекаем 
ребро с максимальным весом и прибавляем вес к итоговому значению. Если по итогу у нас какой-то вершины нет в списке 
обработанных, значит компонентов связанности несколько. В противном случае, выводим итоговое значение веса (не забыв 
заменить минус).

-- Доказательство --
Мы всегда выбираем ребро с максимальным весом и прошодим по всем доступным вершинам, следовательно алгоритм выдает
ожидаемый результат

-- Временная сложность --
Для реализации использована куча, работающая за O(log V), где V - число вершин. Поскольку у нас E ребер, получаем
O(E * log V).

-- Пространственная сложность --
Неориентированный граф в формате списка смежности занимает O(E+V), где V - количество вершин, E - количество рёбер.
Куча занимает O(E). Итого считаем O(E+V)

"""

from typing import List, Tuple
from heapq import heappop, heappush


def add_vertex(v:int, added:List, now_edge:tuple, edges:List) -> None:
    added[v] = True
    for e, w in now_edge:
        if not added[e]:
            heappush(edges, (-w, e))   
    

def read_input() -> Tuple[int, int, List]:
    n, m = map(int, input().split())    
    graph = [[] for i in range(n+1)]
    for i in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    return n, m, graph


def main() -> None:
    n, m, graph = read_input()
    added = [False] * (n+1)   
    edges = []
    maximum_spanning_tree = 0

    added[0] = True
    add_vertex(1, added, graph[1], edges)

    while not all(added) and edges:
        w, v = heappop(edges)
        if not added[v]:
            maximum_spanning_tree += -w
            add_vertex(v, added, graph[v], edges)

    if not all(added):
        print('Oops! I did it again')
    else:
        print(maximum_spanning_tree)


main()
