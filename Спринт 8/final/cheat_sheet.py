# Шпаргалка
# https://contest.yandex.ru/contest/26133/run-report/117295229/

"""
-- Описание --
Сначала из всех символов входных строк создаем префиксное дерево и помечаем терминальные узлы (окончания слов).
Далее создаем массив dp длинны текста + 1. В нулевую ячейку пишем 1 (для пустой строки). Проходим по всем символам 
текста и ищем совпадения в дереве, если дошли до терминального узла в dp ставим 1 индексу, где слово кончается. 

-- Доказательство --
Таким образом, если текст можно составить из слов в последней ячейке dp у нас будет 1, если нельзя, то 0.

-- Временная сложность --
Создание дерева - О(L), где L - суммарное колличество символов в переданных словах.
Проверка текста - О(n^2), где n - длина текста, т.к. имеем внешний цикл по n и вложенный цикл по n/2 (в среднем).
Итого О(L + n^2).

-- Пространственная сложность --
На хранение дерева - O(L), где L - суммарное колличество символов в переданных словах. Из-за хранения признака 
терминальности и исходяших ребер, будет кратно больше, но считаем как O(L).
На dp массив - О(n), где n - длина текста.
Итого О(n + L).

"""

from typing import List, Tuple


class Node:  
    def __init__(self, value, outgoing_edges=None):  
        self.value = value  
        self.outgoing_edges = {} if outgoing_edges is None else outgoing_edges 
        self.is_terminal = False


def сheat_sheet(text: str, strings: List, root: Node) -> int:
    dp = [1] + [0] * len(text)
    for i in range(len(text)):
        node = root
        if dp[i]:
            for j in range(i, len(text) + 1):
                if node.is_terminal:
                    dp[j] = 1
                if j == len(text) or text[j] not in node.outgoing_edges:
                    break        
                node = node.outgoing_edges[text[j]]
        if dp[-1]: 
            return 1
    return dp[-1]


def read_input() -> Tuple[str, List]:
    text = input()
    n = int(input())
    strings = [input() for _ in range(n)]
    return text, strings


def main() -> None:
    text, strings = read_input()
    # создадим дерево
    root = Node('')
    for string in strings:
        node = root
        for symb in string:
            # если значение уже есть, то его же кладем обратно, если нет, создаем узел
            node.outgoing_edges[symb] = node.outgoing_edges.get(symb, Node(symb))
            # переходим в новый узел
            node = node.outgoing_edges[symb]
        node.is_terminal = True
    
    print('YES' if сheat_sheet(text, strings, root) else 'NO')


main()
