def f(array, number):

    greater = 0
    for i in array:
        if i > number:
            greater += 1
    return greater

print(f([1, 2, 3, 4, 5, 6], 4))