# def f(binary_number):
#     for i in binary_number:
#         if i == "1" or i =="0":
#             return True
#         else:
#             return True
        

# f("10101010")





def f(binary_number):
    for i in binary_number:
        if i != "0" and i != "1":
            return False
    return True

print(f("10101010"))  # True
print(f("10201010"))  # False

