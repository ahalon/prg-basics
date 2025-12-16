def f(array, k):
    for i in range(len(array)):
        if array[i] == k:
            return i
    return -1

print(f([1, 5, 8, 5, 3], 8))
print(f([10, 20, 30], 5))
