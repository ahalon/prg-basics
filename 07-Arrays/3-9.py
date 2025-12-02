def compare(array1, array2):
    if len(array1) != len(array2):
        return False
    
    i = 0
    while i < len(array1):
        if array1[i] != array2[i]:
            return False
        i += 1
    
    return True
