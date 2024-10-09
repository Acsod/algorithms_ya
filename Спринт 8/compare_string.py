# Сравнение строк
# Алла придумала новый способ сравнивать две строки: чтобы сравнить строки a и b, в них надо 
# оставить только те буквы, которые в английском алфавите стоят на четных позициях. Затем 
# полученные строки сравниваются по обычным правилам. Помогите Алле реализовать новое 
# сравнение строк.


from string import ascii_lowercase
from typing import List, Tuple


def comp_str(s1: str, s2: str, compape_alf: List) -> int:
    s1 = ''.join([_ for _ in s1 if _ in compape_alf])
    s2 = ''.join([_ for _ in s2 if _ in compape_alf])
    if s1 < s2:
        return -1
    elif s1 > s2:
        return 1
    else:
        return 0


def read_input() -> Tuple[str, str]:
    s1 = input()
    s2 = input()
    return s1, s2


def main() -> None:
    s1, s2 = read_input()
    compape_alf = [ascii_lowercase[i] for i in range(len(ascii_lowercase)) if i % 2 != 0]
    print(comp_str(s1, s2, compape_alf))


main()
