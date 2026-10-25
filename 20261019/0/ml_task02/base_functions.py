from typing import List
from copy import deepcopy


def get_part_of_array(X: List[List[float]]) -> List[List[float]]:
    """Выбрать строки 0, 4, 8, ... и столбцы 120, 125, ..., 495."""
    result = []
    for row in X[::4]:
        result.append(row[120:500:5])
    return result


def sum_non_neg_diag(X: List[List[int]]) -> int:
    """Сложить неотрицательные элементы диагонали; при их отсутствии вернуть -1."""
    total = 0
    found = False
    for i in range(min(len(X), len(X[0]))):
        if X[i][i] >= 0:
            total += X[i][i]
            found = True
    return total if found else -1


def replace_values(X: List[List[float]]) -> List[List[float]]:
    """В копии заменить значения вне [0.25M, 1.5M], где M — среднее столбца."""
    result = deepcopy(X)
    rows = len(X)
    for j in range(len(X[0])):
        total = 0.0
        for i in range(rows):
            total += X[i][j]
        mean = total / rows
        for i in range(rows):
            if X[i][j] < 0.25 * mean or X[i][j] > 1.5 * mean:
                result[i][j] = -1
    return result
