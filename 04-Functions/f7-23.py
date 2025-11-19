# def f(password):
#     already_counted = []
#     pas = ""
#     for i in password:
#         pas += i
#         if i not in already_counted:
#             cnt = pas.count(i)
#         already_counted.append(i)
#         if len(pas) >= 6 and cnt <=1: 
#             return True
#     return False
    
# print(f("ax15"))
# print(f("book123"))
# print(f("qwerty"))


def f(password):
    if len(password) < 6:
        return False

    for char in password:
        if password.count(char) > 1:
            return False  

    return True  

print(f("ax15"))
print(f("book123"))   
print(f("A2water3"))
print(f("qwerty"))
print(f(""))