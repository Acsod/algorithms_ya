# Большое число
# Вечером ребята решили поиграть в игру «Большое число».
# Даны числа. Нужно определить, какое самое большое число можно из них составить.


from typing import List, Tuple


def big_digit(n: int, series: List[int]):
    max_num = max(series)
    answer = ''.join(map(str, sorted(series, reverse=True, key=lambda x: len(str(max_num)) * str(x))))
    return answer
    

def read_input() -> Tuple[int, List]:
    n = int(input())
    series = list(map(int, input().split()))
    return n, series


def main():
    n, series = read_input()
    print(big_digit(n, series))


main()
