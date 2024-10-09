# Стек - Max
# Нужно реализовать класс StackMax, который поддерживает операцию 
# определения максимума среди всех элементов в стеке. Класс должен
# поддерживать операции push(x), где x – целое число, pop() и get_max().


from typing import List, Tuple


class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return 'error'
        return self.items.pop()
    
    def get_max(self):
        if len(self.items) == 0:
            return 'None'
        return max(self.items)
 
    
def read_input() -> Tuple[int, List]:
    n = int(input())
    comands = []
    for i in range(n):
        comands.append(input().split())
    return n, comands


def main():
    n, comands = read_input()
    stack = StackMax()
    for i in range(n):
        if len(comands[i]) > 1:
            eval('stack.'+'('.join(comands[i]) + ')')
        elif comands[i] == ['get_max']:
            print(eval('stack.'+''.join(comands[i]) + '()'))
        else:
            pop_res = eval('stack.'+''.join(comands[i]) + '()')
            if pop_res == 'error':
                print(pop_res)

main()
