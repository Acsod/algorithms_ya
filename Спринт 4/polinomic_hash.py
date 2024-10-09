# Полиномиальный хеш
# Алле очень понравился алгоритм вычисления полиномиального хеша. Помогите ей 
# написать функцию, вычисляющую хеш строки s. В данной задаче необходимо использовать
# в качестве значений отдельных символов их коды в таблице ASCII.


from typing import List, Tuple


def plinonic_hah(a:int, m:int, s:str) -> int:
    polin = 0
    for i in range(len(s)):
        polin = (polin * a + ord(s[i])) % m
    return polin


def read_input() -> Tuple[int, int, str]:
    a = int(input())
    m = int(input())
    s = input()
    return a, m, s


def main():
    a, m, s = read_input()
    print(plinonic_hah(a, m, s))


main()
