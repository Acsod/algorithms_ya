# Нелюбимое дело
# Вася размышляет, что ему можно не делать из того списка дел, который он составил. 
# Но, кажется, все пункты очень важные! Вася решает загадать число и удалить дело, 
# которое идёт под этим номером. Список дел представлен в виде односвязного списка. 
# Напишите функцию solution, которая принимает на вход голову списка и номер удаляемого
# дела и возвращает голову обновлённого списка.


def solution(node, idx):
    head = node
    def get_node_by_idx(head_node, index):
        while index:
            head_node = head_node.next_item
            index -= 1
        return head_node
    if idx == 0:
        return head.next_item
    del_node = get_node_by_idx(head, idx)
    new_link_for_prevous = del_node.next_item
    previous_node = get_node_by_idx(head, idx-1)
    previous_node.next_item = new_link_for_prevous

    return head