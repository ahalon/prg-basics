arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]

new1 = []

for value in arr1:
    if value not in arr2:
        new1.append(value)

print(*new1)
