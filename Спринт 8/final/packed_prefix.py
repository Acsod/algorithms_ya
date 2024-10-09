# Packed Prefix
# https://contest.yandex.ru/contest/26133/run-report/117297275/

"""
-- Описание --
Сначала нам необходимо распаковать входные данные. Для каждой строи входа создадим 2 стека - для цифр и текста, а также строку распаковки.
Будем добавлять в сроку распаковки свободные символы и содержимое скобок, умноженное на числа перед ними. Все распакованные строки добавим
в список и передадим в основную функцию поиска префикса. Максимальный возможный префикс - это самая короткая строка входных данных. Будем
сравнивать строку почередно с префиксами равной длинны других строк. Если есть не совпадение, уменьшаем длину префикса на 1 символ с конца.
Возвращаем итоговую наибольшую общую строку.

-- Доказательство --
Мы сверяем все префиксы и находим наибольший за меньшее время, чем, если бы добавляли символы по одному.

-- Временная сложность --
Время распаковки О(n * L), где L - размер самой длинной строки в запакованном виде. 
Поиск префикса - О(n * l), где l - длина самой короткой строки в распакованном виде.

-- Пространственная сложность --
На хранение входных данных О(n * L), где L - размер самой длинной строки в распакованном виде. На хранение перемееной для префикса l, где 
l - длина самой короткой строки в распакованном виде. То есть можно считать О(n * L).
"""

from typing import List, Tuple

def packed_prefix(n:int, strings: List) -> str:
    strings.sort(key=len) 
    prefix = strings[0]
    len_prefix = len(strings[0])
    i = 1

    while i < n:
        if strings[i].find(prefix) != 0:
            prefix = prefix[:-1]
            i = 1
        else:
            i += 1   
    return prefix


def read_input() -> Tuple[int, str]:
    n = int(input())
    strings = []
    for i in range(n):
        a = input()
        num_stak = []
        brucket_stack = []
        symb_stack = ''
        for i in range(len(a)):
            if a[i].isnumeric():
                num_stak.append(int(a[i]))
            elif a[i] == '[':
                brucket_stack.append([])
            elif a[i].isalpha():
                if brucket_stack:
                    brucket_stack[-1].append(a[i])
                else:
                    symb_stack += a[i]
            elif a[i] == ']':
                bracket = ''.join(brucket_stack.pop())
                substring = num_stak.pop() * bracket
                if brucket_stack:
                    brucket_stack[-1].append(substring)
                else:
                    symb_stack += substring
        strings.append(symb_stack)
    return n, strings


def main() -> None:
    print(packed_prefix(*read_input()))


main()
