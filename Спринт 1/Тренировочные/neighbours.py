# Соседи
# Дана матрица. Нужно написать функцию, которая для элемента возвращает всех его 
# соседей. Соседним считается элемент, находящийся от текущего на одну ячейку 
# влево, вправо, вверх или вниз. Диагональные элементы соседними не считаются.


from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    neighbours = []
    rows_mat = len(matrix)
    cols_mat = len(matrix[0])
    
    if col - 1 >= 0:
        neighbours.append(matrix[row][col-1])
    if col + 1 <= cols_mat - 1:
        neighbours.append(matrix[row][col+1])
    if row - 1 >= 0:
        neighbours.append(matrix[row-1][col])
    if row + 1 <= rows_mat - 1:
        neighbours.append(matrix[row+1][col])

    return sorted(neighbours)


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    _ = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col


matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))
