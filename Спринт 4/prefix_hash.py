# Префиксные хеши
# Алла не остановилась на достигнутом –— теперь она хочет научиться быстро вычислять
# хеши произвольных подстрок данной строки. Помогите ей!
# На вход поступают запросы на подсчёт хешей разных подстрок. Ответ на каждый запрос
# должен выполняться за O(1). Допустимо в начале работы программы сделать предподсчёт 
# для дальнейшей работы со строкой.


from typing import List, Tuple


def prefix_hah(a:int, m:int, s:str, idxs:List[int]) -> List[int]:
    pref_hashs = [0] * (len(s) + 1)
    powers = [1] * (len(s) + 1)
    pref_hashs[1] = ord(s[0]) % m
    for i in range(2, len(pref_hashs)):
        pref_hashs[i] = (pref_hashs[i-1] * a + ord(s[i-1])) % m
        powers[i-1] = (powers[i-2] * a) % m
    for i, j in idxs:
        print((pref_hashs[j] - (pref_hashs[i-1] * powers[j-i+1])) % m)


def read_input() -> Tuple[int, int, str]:
    a = int(input())
    m = int(input())
    s = input()
    n = int(input())
    idxs = []
    for i in range(n):
        idxs.append(list(map(int, input().split())))
    return a, m, s, idxs


def main():
    a, m, s, idxs = read_input()
    prefix_hah(a, m, s, idxs)


main()
