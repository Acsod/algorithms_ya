# Подпоследовательность
# Гоша любит играть в игру «Подпоследовательность»: даны 2 строки, и нужно понять, 
# является ли первая из них подпоследовательностью второй. Когда строки достаточно 
# длинные, очень трудно получить ответ на этот вопрос, просто посмотрев на них. 
# Помогите Гоше написать функцию, которая решает эту задачу.


from typing import List, Tuple

def is_sequence(s, t):
    inx = -1
    for a in s:
        inx = t.find(a, inx + 1)
        if inx == -1:
            return False     
    return True
 

def read_input() -> Tuple[str, str]:
    s = input()
    t = input()
    return s, t


def main():
    s, t = read_input()
    print(is_sequence(s, t))


main()
