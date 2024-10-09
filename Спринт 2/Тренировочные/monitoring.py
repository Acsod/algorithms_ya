# Мониторинг
# Алла получила задание, связанное с мониторингом работы различных серверов. 
# Требуется понять, сколько времени обрабатываются определённые запросы на 
# конкретных серверах. Эту информацию нужно хранить в матрице, где номер 
# столбца соответствуют идентификатору запроса, а номер строки — идентификатору
# сервера. Алла перепутала строки и столбцы местами. С каждым бывает. 
# Помогите ей исправить баг.
# Есть матрица размера m × n. Нужно написать функцию, которая её транспонирует.


from typing import List, Tuple


def transpose(matrix: List[List[int]], row: int, col: int) -> None:
    for i in range(col):
        new_row = []
        for j in range(row):
            new_row.append(matrix[j][i])
        print(" ".join(map(str, new_row)))



def read_input() -> Tuple[List[List[int]], int, int]:
    row = int(input())
    col = int(input())
    matrix = []
    for _ in range(row):
        matrix.append(list(map(int, input().strip().split())))
    return matrix, row, col


def main():
    matrix, row, col = read_input()
    transpose(matrix, row, col)


main()