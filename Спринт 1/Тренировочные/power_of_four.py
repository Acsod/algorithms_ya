# Степень четырёх
# Напишите программу, которая определяет, будет ли положительное целое число степенью четвёрки.
# Подсказка: степенью четвёрки будут все числа вида 4^n, где n – целое неотрицательное число.


def is_power_of_four(number: int) -> bool:
    mult = 1
    while mult < number:
        mult *= 4
    return mult == number


print(is_power_of_four(int(input())))
