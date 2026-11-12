import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    ans=[]
    rows = len(matrix)
    cols = len(matrix[0])
    if mode=='row':
        ans = np.sum(matrix, axis=1)/(1.0*cols)
    else:
        ans = np.sum(matrix, axis=0)/(1.0*rows)

    return ans