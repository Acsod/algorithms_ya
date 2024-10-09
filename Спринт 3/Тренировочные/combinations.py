# Комбинации
# На клавиатуре старых мобильных телефонов каждой цифре соответствовало несколько букв. Примерно так:
#   2:'abc',
#   3:'def',
#   4:'ghi',
#   5:'jkl',
#   6:'mno',
#   7:'pqrs',
#   8:'tuv',
#   9:'wxyz'
# Вам известно в каком порядке были нажаты кнопки телефона, без учета повторов. Напечатайте все комбинации букв, которые можно набрать такой последовательностью нажатий.


from typing import List, Tuple

def gen(lavels, list_str, counter, result, all_list):
    if counter == lavels:
        all_list.append(result)
        return result
    for i in list_str[counter]:
        gen(lavels, list_str, counter+1, result + i, all_list)
        
    return all_list

def read_input() -> List[int]:
    digit = list(map(int, [i for i in input()]))
    digit_dict = {
        2:'abc',
        3:'def',
        4:'ghi',
        5:'jkl',
        6:'mno',
        7:'pqrs',
        8:'tuv',
        9:'wxyz'}
    letters = [digit_dict[i] for i in digit]   
    return letters


def main():
    letters = read_input()
    answer = gen(len(letters), letters, counter=0, result='', all_list=[])
    print(' '.join(answer))


main()
