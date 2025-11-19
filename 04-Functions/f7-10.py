def f(x,y):
    total = 0
    for i in range(x, y+1):        
        if i % 2 == 0 and i < 0:
            total += 1
    return total

print(f(-7, 8))








