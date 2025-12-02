arr = [15, 8, 31, 47, 2, 19]

print("Existed array:", *arr)

rev = []
i = len(arr) - 1

while i >= 0:
    rev.append(arr[i])
    i-= 1

print("reverse array:", *rev)