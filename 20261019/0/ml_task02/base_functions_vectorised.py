import numpy as np


def get_part_of_array(X: np.ndarray) -> np.ndarray:
    """Выбрать нужные строки и столбцы двумерным срезом."""
    return X[::4, 120:500:5]


def sum_non_neg_diag(X: np.ndarray) -> int:
    """Сложить неотрицательные элементы диагонали; при их отсутствии вернуть -1."""
    diagonal = np.diagonal(X)
    non_negative = diagonal[diagonal >= 0]
    return int(non_negative.sum()) if non_negative.size else -1


def replace_values(X: np.ndarray) -> np.ndarray:
    """Применить пороги по столбцам, сохранив исходный массив."""
    means = X.mean(axis=0)
    result = X.copy()
    result[(X < 0.25 * means) | (X > 1.5 * means)] = -1
    return result
