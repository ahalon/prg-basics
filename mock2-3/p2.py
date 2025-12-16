def f(matrix):
    n = len(matrix)
    anti_diag = []
    for i in range(n):
        anti_diag.append(matrix[i][n - 1 - i])
    return min(anti_diag)
