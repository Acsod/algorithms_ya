# Ограниченная очередь
# Астрологи объявили день очередей ограниченного размера. Тимофею нужно 
# написать класс MyQueueSized, который принимает параметр max_size, 
# означающий максимально допустимое количество элементов в очереди.
# Помогите ему —– реализуйте программу, которая будет эмулировать 
# работу такой очереди. Функции, которые надо поддержать, описаны 
# в формате ввода.


from typing import List, Tuple


class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.head = 0
        self.tail = 0
        self.max_size = max_size
        self.size_now = 0

    def push(self, item):
        if self.size_now != self.max_size:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_size
            self.size_now += 1
        else:
            print('error')

    def pop(self):
        if self.size_now == 0:
            print(None)
        else:
            item = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_size
            self.size_now -= 1
            print(item)
    
    def peek(self):
        if self.size_now == 0:
            print(None)
        else:
            item = self.queue[self.head]
            print(item)
    
    def size(self):
        print(self.size_now)
 
    
def read_input() -> Tuple[int, List]:
    n = int(input())
    max_size = int(input())
    comands = []
    for i in range(n):
        comands.append(input().split())
    return n, max_size, comands


def main():
    n, max_size, comands = read_input()
    stack = MyQueueSized(max_size)
    for i in range(n):
        if len(comands[i]) > 1:
            eval('stack.'+'('.join(comands[i]) + ')')
        else:
            eval('stack.'+''.join(comands[i]) + '()')

main()
