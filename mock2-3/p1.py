def f(arr):
    str_max = max(arr)
    count = 0 
    for i in arr:
        if i == str_max:
            count += 1
    return count

print(f([10, 5, 20, 15, 20, 8]))