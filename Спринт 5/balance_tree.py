# Сбалансированное дерево
# Гоше очень понравилось слушать рассказ Тимофея про деревья. Особенно часть 
# про сбалансированные деревья. Он решил написать функцию, которая определяет, 
# сбалансировано ли дерево.
# Дерево считается сбалансированным, если левое и правое поддеревья каждой вершины 
# отличаются по высоте не больше, чем на единицу.


import os


LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:  
        def __init__(self, value, left=None, right=None):  
            self.value = value  
            self.right = right  
            self.left = left


def max_high(root):
    if root is None:
        return 0
    return max(max_high(root.left), max_high(root.right)) + 1 


def solution(root) -> bool:
    if root is None:
        return True
    h_l = max_high(root.left)
    h_r = max_high(root.right)
    if abs(h_l - h_r) <= 1:
        return solution(root.left) and  solution(root.right)
    else:
        return False
    

def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == '__main__':
    test()
    