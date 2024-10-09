# Сломай меня
# Гоша написал программу, которая сравнивает строки исключительно по их хешам. Если хеш равен,
# то и строки равны. Тимофей увидел это безобразие и поручил вам сломать программу Гоши, чтобы 
# остальным неповадно было.
# В этой задаче вам надо будет лишь найти две различные строки, которые для заданной хеш-функции 
# будут давать одинаковое значение

import random
from typing import List, Tuple
from string import ascii_letters

def plinonic_hah(a:int, m:int, s:str) -> int:
    polin = 0
    for i in range(len(s)):
        polin = (polin * a + ord(s[i])) % m
    return polin


def generate_crash(a:int, m:int) -> Tuple[str, str]:
    log = {}
    alphas = ascii_letters[:len(ascii_letters)//2]
    while True:
        len_str = random.choice(range(5, 25))
        val = ''.join([random.choice(alphas) for x in range(len_str)])
        hash = plinonic_hah(a, m, val)
        if (hash in log) and (log[hash] != val):
            return val, log[hash]
        else:
            log[hash] = val


def main():
    a = int(1000)
    m = int(123987123)
    print(generate_crash(a, m))


main()
