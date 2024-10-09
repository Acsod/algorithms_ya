# Вставка строк
# У Риты была строка s, Гоша подарил ей на 8 марта ещё n других строк ti, 1≤ i≤ n. Теперь Рита думает,
# куда их лучше поставить. Один из вариантов —– расположить подаренные строки внутри имеющейся строки s,
# поставив строку ti сразу после символа строки s с номером ki (в частности, если ki=0, то строка 
# вставляется в самое начало s).
# Помогите Рите и определите, какая строка получится после вставки в s всех подаренных Гошей строк.


from typing import List


def insert_str(s: str, gifts: List) -> str:
    gifts.sort(key=lambda x: x[1])
    new_str = ''
    start = 0
    for s_gift, idx in gifts:
        new_str += s[start:idx] + s_gift
        start = idx
    if start < len(s):
        new_str += s[start:]
    return new_str


def read_input() -> List:
    s = input()
    n = int(input())
    gifts = []
    for i in range(n):
        val1, val2 = input().split()
        gifts.append((val1, int(val2)))
    return s, gifts


def main() -> None:
    print(insert_str(*read_input()))


main()
