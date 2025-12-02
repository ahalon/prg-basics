def f(arr1, arr2):
    for j in arr1:
        if j not in arr2:
            return False
    return True
