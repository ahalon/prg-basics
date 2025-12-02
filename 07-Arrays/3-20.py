def separate_even_odd(arr):
    even = []
    odd = []
    for n in arr:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)
    return even + odd

# sample
arr = [7, 9, 2, 4, 5, 6]
arr = separate_even_odd(arr)
print(arr)   # [2, 4, 6, 7, 9, 5]
