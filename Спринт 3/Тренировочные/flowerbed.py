# Клумбы
# Алла захотела, чтобы у неё под окном были узкие клумбы с тюльпанам. На схеме земельного
# участка клумбы обозначаются просто горизонтальными отрезками, лежащими на одной прямой. 
# Для ландшафтных работ было нанято n садовников. Каждый из них обрабатывал какой-то отрезок 
# на схеме. Процесс был организован не очень хорошо, иногда один и тот же отрезок или его 
# часть могли быть обработаны сразу несколькими садовниками. Таким образом, отрезки, 
# обрабатываемые двумя разными садовниками, сливаются в один. Непрерывный обработанный 
# отрезок затем станет клумбой. Нужно определить границы будущих клумб.


from typing import List, Tuple
from collections.abc import Iterable


def flowerbed(n, arr):
    if n == 1:
        return arr
    
    arr.sort(key=lambda x: (x[0], -x[1]))
    res = []
    cur = arr[0]
    for item in arr[1:]:
        if cur[1] < item[0]:
            res.append(cur)
            cur=item
        else:
            cur[1] = max(cur[1], item[1])
    res.append(cur)

    return res
    

def read_input() -> Tuple[int, List[List[int]]]:
    n = int(input())
    series = []
    for i in range(n):
        series.append(list(map(int, input().split())))
    return n, series


def main():
    n, series = read_input()
    answer = flowerbed(n, series)
    answer = [' '.join(map(str, x)) for x in answer]
    print(*answer, sep='\n')


main()
