# Заботливая мама
# Мама Васи хочет знать, что сын планирует делать и когда. Помогите ей: 
# напишите функцию solution, определяющую индекс первого вхождения 
# передаваемого ей на вход значения в связном списке, если значение присутствует.


def solution(node, elem):
    index = 0
    while node.next_item:
        if node.value == elem:
            return index
        index += 1
        node = node.next_item
    return -1