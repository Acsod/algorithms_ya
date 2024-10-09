# Работа из дома
# Вася реализовал функцию, которая переводит целое число из десятичной системы в двоичную. 
# Но, кажется, она получилась не очень оптимальной.
# Попробуйте написать более эффективную программу.
# Не используйте встроенные средства языка по переводу чисел в бинарное представление.


def to_binary(number: int) -> str:
    if number > 0:
        t = [number>>i & 1 for i in range(14)]
        t.reverse()
        return ''.join(map(str, t[t.index(1):]))
    return 0


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
