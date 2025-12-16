def f(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i
        
print(f([7,7,7,7,7,5,7,7]))
        
