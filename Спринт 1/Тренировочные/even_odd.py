# Чётные и нечётные числа
# Представьте себе онлайн-игру для поездки в метро: игрок нажимает на кнопку, и на 
# экране появляются три случайных числа. Если все три числа оказываются одной чётности, 
# игрок выигрывает.
# Напишите программу, которая по трём числам определяет, выиграл игрок или нет.


def check_parity(a: int, b: int, c: int) -> bool:
    if ((a % 2 == 0) & (b % 2 == 0) & (c % 2 == 0)) | ((a % 2 != 0) & (b % 2 != 0) & (c % 2 != 0)):
        return True
    else:
        return False


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")


a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
