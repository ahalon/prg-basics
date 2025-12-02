arr = [8, 2, 5, 1, 9]

print("Array:", *arr)

squared = []
i = 0

while i < len(arr):
    squared.append(arr[i] ** 2)
    i += 1

print("2nd power:", *squared)

