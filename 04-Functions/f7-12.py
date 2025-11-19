def f(n):
    return "/".join(["*"] * n)

print(f(4))  # "*/*/*/*"
print(f(1))  # "*"


# def f(n):
#     result = ""  # pusty string na start
#     for i in range(n):
#         if i > 0:
#             result += "/"  # dodajemy slash **tylko po pierwszej gwiazdce**
#         result += "*"     # dodajemy gwiazdkę
#     return result

# print(f(4))  # "*/*/*/*"
# print(f(1))  # "*"
