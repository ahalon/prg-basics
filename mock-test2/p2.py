def f(arr):

    
    if arr[0] != arr[1] and  arr[1] == arr[2]:
        return arr[0]
    elif arr[0] != arr[1] and  arr[1] != arr[2]:
        return arr[1]
    else:
        common = arr[0]
        for i in arr:
            if i != common:
                return i



print(f([7,7,7,7,7,5,7,7]))
