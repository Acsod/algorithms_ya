# Поиск со сдвигом
# Гоша измерял температуру воздуха n дней подряд. В результате у него получился некоторый временной ряд.
# Теперь он хочет посмотреть, как часто встречается некоторый шаблон в получившейся последовательности. 
# Однако температура — вещь относительная, поэтому Гоша решил, что при поиске шаблона длины m (a1, a2, ..., am)
# стоит также рассматривать сдвинутые на константу вхождения. Это значит, что если для некоторого числа c в 
# исходной последовательности нашёлся участок вида (a1 + c, a2 + c, ... , am + c), то он тоже считается вхождением 
# шаблона (a1, a2, ..., am).
# По заданной последовательности измерений X и шаблону A=(a1, a2, ..., am) определите все вхождения A в X, 
# допускающие сдвиг на константу.


from typing import List, Tuple


def find_with_shift(n:int, s1: str, m: int, s2: str) -> str:
    answer = []
    if m > n:
        raise ValueError('Шаблон длиннее строки поиска')
    for pos in range(len(s2) - 1, len(s1)):
        offset = pos - (len(s2) - 1)
        slice = s1[offset : pos + 1]
        diff = set((x - y for x, y in zip(slice, s2)))
        if len(diff) == 1:
            answer.append(offset + 1)
    return ' '.join(map(str, answer))


def read_input() -> Tuple[str, str]:
    n = int(input())
    s1 = list(map(int, input().split()))
    m = int(input())
    s2 = list(map(int, input().split()))
    return n, s1, m, s2


def main() -> None:
    print(find_with_shift(*read_input()))


main()
