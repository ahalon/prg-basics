def f(n):
    result=""
    for i in range(1,n+1):
        str_n = str(i)
        result += str_n
        res_str = str(result)
    return res_str

print(f(11))
