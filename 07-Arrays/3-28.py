# dwuwymiarowa tablica
arr = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

# sumowanie ostatniej kolumny
last_col_sum = 0
for row in arr:
    last_col_sum += row[-1]  # -1 oznacza ostatni element w wierszu

print("Suma wartości w ostatniej kolumnie:", last_col_sum)
