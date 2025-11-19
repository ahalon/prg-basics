def f(product_code):
    n1 = int(product_code[0])
    n2 = int(product_code[1])
    n3 = int(product_code[2])
    n4 = int(product_code[3])
    sum_3 = n1 + n2 + n3
    if sum_3 % 7 == n4:
        return True
    else:
        return False

print(f("1082"))
print(f("1114"))