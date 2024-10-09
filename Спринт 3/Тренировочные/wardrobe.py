# Гардероб
# Рита решила оставить у себя одежду только трёх цветов: розового, жёлтого и малинового.
# После того как вещи других расцветок были убраны, Рита захотела отсортировать свой 
# новый гардероб по цветам. Сначала должны идти вещи розового цвета, потом —– жёлтого,
# и в конце —– малинового. Помогите Рите справиться с этой задачей.


from typing import List, Tuple

def count_sort(n, series):
    count_list = [0] * 3
    new_ser = []
    for i in series:
        count_list[i] += 1

    index = 0
    for color in range(3):        
        for element in range(count_list[color]):
            series[index] = color
            index += 1   
                     
    return series
 

def read_input() -> Tuple[str, List]:
    n = input()
    series = list(map(int, input().split()))
    return n, series


def main():
    n, series = read_input()
    print(' '.join(map(str, count_sort(n, series))))


main()
