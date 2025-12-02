arr = [15, 8, 31, 47, 2, 19]

sum_arr = 0
quantity_arr = 0
i = 0

while i < len(arr):
    sum_arr += arr[i]
    quantity_arr += 1
    i += 1  

arithmetic_mean = sum_arr / quantity_arr

print(f'arithmetic mean: {arithmetic_mean}')