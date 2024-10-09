# Хеш-таблица
# https://contest.yandex.ru/contest/24414/run-report/115862276/

"""
-- Описание --
Реализована хэш-таблица (MyHashTable) с capacity по умолчанию 100003 и самой таблицей - список None длинной capacity. Разрешение колизий 
организовано методом цепочек. Создан вспомагательный класс MyNode для удобства хранения ключа и значения (можно реализовать простым tuple, но не так читаемо). Внутри класса 
MyHashTable описаны методы put, get, delete и скрытый метод __get_hash__ для получения хэша (использована стандартная функция hash (для 
значени целочисленных значений возвращает их самих), которую, в целом, можно опустить, если исходить из условий задачи (только int)).

-- Доказательство --
Метод put принимает на вход ключ и значение, по ключу получает хэш (по сути - модуль целочисленного значения на capacity таблицы) - он же
индекс ячейки. Если ячейка пуста, в нее помещается список со значением в виде узла (ключ, значение). Если ячейка по хэшу не пуста, проходим 
по внутренниму списку и проверяем ключи. ЕСли ключ совпал - обновляем его значение. Если совпадающего ключа не нашлось, создаем новый узел
и добавляем в конц списка.
Метод get получает на вход ключ, по ключу получает хэш, проверяет ячейку по хэшу, если там список, проходит по нему и, если находит ключ, 
возвращает значение. В противном случае возвращает None.
Метод delete олучает на вход ключ, по ключу получает хэш, проверяет ячейку по хэшу, если там список, проходит по нему и, если находит ключ, 
возвращает значение, удаляя найденный узел. В противном случае возвращает None.

-- Временная сложность --
За счет доступа к ячейкам по хэшу и размеру хэш-таблицы capacity 10^5, большая часть операций выполняется за О(n). В случае возникновения 
коллизии, конкретная операция может выполняться за О(1 + k), где k - количество ключей, имеющий такой же хэш. В нашем случае одинаковый 
хэш будут иметь числа кратные 100003 (простое число), каковых не много. При большом числе запросов, аммартизированным временем исполнения
любой операции можем считать О(n)

-- Пространственная сложность --
Пусть n - это количество пар ключ/значение. Для создания пустой таблицы использован список размера capacity (константа, пусть будет k). 
Для каждого узла используется 2 int-а, то есть n. Есть до расходы на создание списка узлов, т.к. каждый список (массив что-то весит), но
в целом можем считать, что расходуем k + n памяти.

"""

from typing import List, Tuple


class MyNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class MyHashTable:
    def __init__(self, capacity=133337):
        self.capacity = capacity
        self.cells = [None] * capacity

    def __get_hash__(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        idx = self.__get_hash__(key)
        if self.cells[idx] is None:
            self.cells[idx] = [MyNode(key, value),]
        else:
            nodes = self.cells[idx]
            for i in range(len(nodes)):
                if nodes[i].key == key:
                    nodes[i].value = value
                    return
            self.cells[idx].append(MyNode(key, value))
            
    def get(self, key):
        idx = self.__get_hash__(key)
        nodes = self.cells[idx]
        if nodes:
            for i in range(len(nodes)):
                if nodes[i].key == key:
                    return nodes[i].value
        return                                # решила оставить исходя из "явное лучше чем не явное"
        
    def delete(self, key):
        idx = self.__get_hash__(key)
        nodes = self.cells[idx]
        if nodes:
            for i in range(len(nodes)):
                if nodes[i].key == key:
                    return nodes.pop(i).value
        return


def main():
    n = int(input())
    hash_table = MyHashTable()
    for i in range(n):
        comand = input().split()
        if comand[0] == 'put':
            hash_table.put(comand[1], comand[2])
        elif comand[0] == 'get':
            print(hash_table.get(comand[1]))
        elif comand[0] == 'delete':
            print(hash_table.delete(comand[1]))
        else:
            print('error')

main()