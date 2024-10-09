# Лампочки
# Гоша повесил на стену гирлянду в виде бинарного дерева, в узлах которого находятся лампочки.
# У каждой лампочки есть своя яркость. Уровень яркости лампочки соответствует числу, 
# расположенному в узле дерева. Помогите Гоше найти самую яркую лампочку в гирлянде, то есть
# такую, у которой яркость наибольшая.


import os
import numpy as np


LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root , max_val=-np.inf) -> int:
    if root is None:
        return
    if root.value > max_val:
        max_val = root.value
    if root.left:    
        max_val = solution(root.left, max_val)
    if root.right: 
        max_val = solution(root.right, max_val)
    return max_val


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


if __name__ == '__main__':
    test()
    