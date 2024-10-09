# Кружки
# В компании, где работает Тимофей, заботятся о досуге сотрудников и устраивают 
# различные кружки по интересам. Когда кто-то записывается на занятие, в лог 
# вносится название кружка.
# По записям в логе составьте список всех кружков, в которые ходит хотя бы один человек.


from typing import List, Tuple


def counter_craft(hobbys: List) -> List:
    map_d = {}
    for hobby in hobbys:
        if hobby in map_d.keys():
            map_d[hobby] += 1
        else:
            map_d[hobby] = 1
            print(hobby)


def read_input() -> Tuple[str, List]:
    n = int(input())
    hobby = []
    for i in range(n):
        hobby.append(input())
    return n, hobby


def main():
    n, hobbys = read_input()
    counter_craft(hobbys)


main()
