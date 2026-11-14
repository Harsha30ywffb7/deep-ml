import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    a = np.array(matrix)
    eigenvalues, eigenvectors = np.linalg.eig(a)
    return np.real(eigenvalues).tolist()