# def f(array2D):
#     n = len(array2D)
#     for i in range(n):
#         row_sum = sum(array2D[i])
#         col_sum = sum(array2D[j][i] for j in range(n))
#     return row_sum == col_sum

# print(f([[3,7,2],[4,2,5],[5,2,1]]))
# print(f([[3,7,2],[4,2,5],[9,2,1]]))


arr = [
    [3, 8, 1],
    [9, 2, 7],
    [4, 6, 5]
]

# pierwsza koklumna
# for i in range (len(arr)):
#     print(arr[i][0])

#suma tzreciego wiersza

sum(arr[2][])

#Policz sumę drugiej kolumny
for j in range(len(arr))
sum3 = sum(arr[j][2] for j in range(len(arr)))


#Wypisz element znajdujący się na wiersz 1, kolumna 2.

# print(arr[0][1])

#Wypisz elementy drugiej przekątnej (arr[0][3], arr[1][2], arr[2][1], arr[3][0])

for i in range (len(arr)):
    print(arr[i][i])
