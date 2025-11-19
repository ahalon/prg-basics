def f(n):
    n_palindrome = n[::-1]
    if n_palindrome ==n:
        return True
    else:
        return False
    

print(f("radar"))
print(f("book"))