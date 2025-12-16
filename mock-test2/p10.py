def f(array):
    min_value = array[0][0]
    min_row = 0
    min_col = 0

    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] < min_value:
                min_value = array[i][j]
                min_row = i
                min_col = j

    return min_row == min_col

