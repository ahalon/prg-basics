arr = [-15, 8, -31, 47, -2, 19]


minimum = arr[0]
maximum = arr[0]

i = 1
while i < len(arr):
    if arr[i] < minimum:
        minimum = arr[i]
    if arr[i] > maximum:
        maximum = arr[i]
    i += 1

print("min =", minimum)
print("max =", maximum)
