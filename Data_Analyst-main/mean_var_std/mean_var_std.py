import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        array = np.array(list)
        matrix = array.reshape(3,3)

        mean = [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix).tolist()]
        var = [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix).tolist()]
        std = [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix).tolist()]
        max = [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix).tolist()]
        min = [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix).tolist()]
        sum = [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix).tolist()]

        matrix_calculations = {
            "mean": mean,
            "variance": var,
            "standard deviation": std,
            "max": max,
            "min": min,
            "sum": sum
        }
        return matrix_calculations