# Всё наоборот
# Вася решил запутать маму —– делать дела в обратном порядке. Список 
# его дел теперь хранится в двусвязном списке. Напишите функцию, 
# которая вернёт список в обратном порядке.


def solution(node):
    while node.next:
        node.buf = node.prev
        node.prev = node.next
        node.next = node.buf
        node = node.prev
    node.buf = node.prev
    node.prev = node.next
    node.next = node.buf
    return node