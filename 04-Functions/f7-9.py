def f(number, even):
    total = 0
    str_num = str(number)
    for i in str_num:
        digit = int(i)
        if even:
            if digit % 2 == 0:
                total += digit
                
        elif not even:
            if digit % 2 !=0:
                total += digit
    return total
                
            
print(f(3124, False))