arr = [2, 3, 2, 5, 8, 1, 9, 8]

unique = []
for value in arr:
    cnt = arr.count(value)
    if cnt == 1:
        unique.append(value)

print(*unique)
        