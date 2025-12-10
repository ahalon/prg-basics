def create_2d_arr(x, y):
    arr = []
    for i in range(x):
        arr.append([0] * y)
    return arr

# Tworzymy tablicę 3x5
my_array = create_2d_arr(3, 5)

# Ładny wydruk w formie tabelki
for row in my_array:
    print(row)


