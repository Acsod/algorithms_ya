# Подсчёт префикс-функции
# В этой задаче вам необходимо посчитать префикс-функцию для заданной строки.


def prefix_function(s: str) -> str:
    n = len(s)
    prefix = [0] + [None] * (n-1)
    for i in range(1, n):
        k = prefix[i - 1]
        while k > 0 and s[k] != s[i]:
            k = prefix[k - 1]
        if s[k] == s[i]:
            k += 1
        prefix[i] = k
    
    return ' '.join(map(str, prefix))


def read_input() -> str:
    s = input()
    return s


def main() -> None:
    print(prefix_function(read_input()))


main()
