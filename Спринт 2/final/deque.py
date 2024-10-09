# A.Дек
# https://contest.yandex.ru/contest/22781/run-report/114730855/

"""
-- Описание --
Реализован дек фиксированной длины с кольцевым буфером.
Изначально индексы головы и хвоста устанавливаем в соседние ячейки 0 и -1, чтобы избежать лишних проверок и сдвигов. 
При добавлении элемента в конец, если не достигнута максимальная длина, записываем элемент в место указателя хвоста и сдвигаем 
указатель по часовой стрелке, чтобы оказаться в пустой ячейке для следующей записи. Не пусто будет только если дек заполнен.
При добавлении элемента в начало, если не достигнута максимальная длина, записываем элемент в место указателя головы и сдвигаем 
указатель против часовой стрелки, чтобы оказаться в пустой ячейке для следующей записи. Не пусто будет только если дек заполнен.
При удалении из начала, если дек не пуст, сначала сдвигаем элемент по часовой стрелке (возвращаемся на последний не пустой слот
от начала), потом удаляем. Указатель снова оказывается на пустом слоте и готов для записи.
Аналогично при удалении из конца, только сдвиг против часовой стрелки.

-- Доказательство --
При такой организации работы с индексами получаем, что запись всегда происходит в пустую ячейку, а указатели пересекаются
только в случае, когда осталась одна пустая ячейка. Удаление и добавление элементов может осуществляться с обоих концов по 
методу LIFO.

-- Временная сложность --
Добавление и удаление элементов производится за О(1), т.к. дек реализован на базе массива и все операции производятся по индексам.
Количество обращений к деку равно n, то есть общая сложность O(n).

-- Пространственная сложность --
Для дэка выделяется О(m) памяти, где m - параметр max_size дэка. Также используются 4 константы равные 1 для хранения параметров 
дэка. Их можно не учитывать. При удалении элемента создается дополнительная переменная item размер которой равен одному из 
элементов массива. Тоже можно не учитывать. Другие структуры не сосздаются.

"""

from typing import List, Tuple


class MyDeque:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.head = -1
        self.tail = 0
        self.max_size = max_size
        self.size_now = 0

    def push_back(self, item):
        if self.size_now != self.max_size:
            self.queue[self.tail] = item
            self.size_now += 1
            self.tail = (self.tail + 1) % self.max_size
        else:
            raise Exception('Deque overflowing')

    def push_front(self, item):
        if self.size_now != self.max_size:
            self.queue[self.head] = item
            self.size_now += 1
            self.head = (self.head - 1) % self.max_size
        else:
            raise Exception('Deque overflowing')

    def pop_front(self):
        if self.size_now == 0:
            raise Exception('Deque empty')
        else:
            self.head = (self.head + 1) % self.max_size
            item = self.queue[self.head]
            self.queue[self.head] = None
            self.size_now -= 1
            return item

    def pop_back(self):
        if self.size_now == 0:
            raise Exception('Deque empty')
        else:
            self.tail = (self.tail - 1) % self.max_size
            item = self.queue[self.tail]
            self.queue[self.tail] = None
            self.size_now -= 1
            return item
 
    
def read_input() -> Tuple[int, int, List]:
    n = int(input())
    max_size = int(input())
    comands = []
    for i in range(n):
        comands.append(input().split())
    return n, max_size, comands


def main():
    n, max_size, comands = read_input()
    stack = MyDeque(max_size)
    for i in range(n):
        try:
            if len(comands[i]) > 1:
                eval('stack.'+'('.join(comands[i]) + ')')
            else:
                print(eval('stack.'+''.join(comands[i]) + '()'))
        except:
            print('error')

main()
