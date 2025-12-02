def f(tuple, value):
    for i in tuple:
        if i == value:
            cnt = tuple.count(i)
    return cnt

print(f((50,20,40,50,30,50), 50))