def f(name):
    result = ""
    splited = name.split()
    for i in splited:
        result += i[0]
    return "".join(result)

print(f("Internet of Things"))