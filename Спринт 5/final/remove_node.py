# Удали узел
# https://contest.yandex.ru/contest/24810/run-report/116184615/

"""
-- Описание --
Написан алгоритм удаления узла из бинарного дерева поиска remove и вспомогательные функции search_remove и search_insert. Сначала в дереве
находим удаляемый элемент remove_node и его родителя remove_node_parent. Если такого элемента нет, возвращаем корень дерева без каких-либо
изменений. Если элемент найден, определяем, еслть ли у него потомки. Если потомков нет, значит заменять удаляемый узел не на что (узел 
вставки insert_node = None), если есть потомки, смотрим есть ли правый потомок, если да - ищем insert_node - самый левый элемент с правой 
стороны, и его родителя. Если нет правого ребенка, ищем слева самый правый элемент и его родителя. Если у insert_node был ребенок (может 
быть только один), переносим сироту к родителю insert_node (insert_node_parent) на место insert_node.
Узлу insert_node, если он есть, переносим детей remove_node.
Если remove_node_parent не существует, значит удаляемый элемент - корень. Меняем root на insert_node.
Если remove_node_parent существует, смотрим левым или правым его ребенком является remove_node и заменяем remove_node на insert_node в 
соответсвующем месте. 
Чтобы remove_node не висел в памяти, заменяем его на None.

-- Доказательство --
Описанный выше алгоритм позволяет удалить узел при его наличии и сохранить дерево в формате BST, т.к. узел либо удаляется безшовно (лист),
либо заменяется максимальным элементом левого поддерева (минимальным элементом правого поддерева). Также учтены варианты с отсутсвием искомого
узла и случаи, когда удаляемый узел является корнем.

-- Временная сложность --
Поиск удаляемого элемента работает за О(h). Поиск элемента для вставки в худшем случае работает за О(h-1). Остальные операции выполняются 
примерно за О(1). То есть итоговая сложность алгоритма - О(h).

-- Пространственная сложность --
Алгоритм реализован без рекурсии. Дополнительная память используется только для храниения remove_node, remove_node_parent, insert_node, 
insert_node_parent по О(1). Можем считать, что потребляем О(1) дополнительной памяти.

"""

from typing import Optional, Tuple
import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value
else:
    from node import Node

    
def search_remove(root, key, parent=None) -> Tuple:
    while root:
        # print(root.value)
        if root.value == key:
            return root, parent
        parent = root
        if root.value < key:
            root = root.right
        elif root.value > key:
            root = root.left
    return None, None

    
def search_insert(root, parent, serch_type='right') -> Tuple:
    if serch_type == 'right':
        while root.right:
            parent = root
            root = root.right
        return root, parent   

    elif serch_type == 'left':
        while root.left:
            parent = root
            root = root.left
        return root, parent    
    
    else:
        raise Exception('Select serch_type is "left" or "right"')
    

def remove(root, key) -> Optional[Node]:
    # находим узел для удаления и его родителя
    remove_node, remove_node_parent = search_remove(root, key)
    # если такого узла нет, возвращаем текущий корень
    if remove_node is None:
        return root
    # если у узла нет потомков, вствлять нечего
    if remove_node.right is None and remove_node.left is None:
        insert_node = None
    # если у узла есть потомки - смотрим слева или справа и находим подходящий элемент на замену и его родителя, затем удаляем ссылку на него
    else:
        if remove_node.right:
            insert_node, insert_node_parent = search_insert(remove_node.right, remove_node, serch_type='left')
            # присваиваем ребенка перемещаемого узла (если таковой есть) родителю. У нас может быть только правый ребенок
            if insert_node == insert_node_parent.left:
                insert_node_parent.left = insert_node.right
            else:
                insert_node_parent.right = insert_node.right
        else:
            insert_node, insert_node_parent = search_insert(remove_node.left, remove_node, serch_type='right')
            # присваиваем ребенка перемещаемого узла (если таковой есть) родителю. У нас может быть только левый ребенок
            if insert_node == insert_node_parent.left:
                insert_node_parent.left = insert_node.left
            else:
                insert_node_parent.right = insert_node.left
    # если узел для вставки найден, присваеваем ему детей удаляемого узла
    if insert_node:
        insert_node.right = remove_node.right
        insert_node.left = remove_node.left
    # если у удоляемого узла нет родителя, значит это корень
    if not remove_node_parent:
        root = insert_node
    # если родитель есть, меняем ссылку на новый узел
    elif remove_node_parent.right == remove_node:
        remove_node_parent.right = insert_node
    else:
        remove_node_parent.left = insert_node
    # дропнем удаленный узел
    remove_node = None
    # возвращаем корень
    return root


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    newHead = remove(node7, 10)
    assert newHead.value == 5
    assert newHead.right is node5
    assert newHead.right.value == 8


if __name__ == '__main__':
    test()
