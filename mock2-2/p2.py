def f(matrix):
    sum_diagonal = 0
    for i in range(len(matrix)):
        sum_diagonal += matrix[i][i]
    return sum_diagonal

print(f([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

        
