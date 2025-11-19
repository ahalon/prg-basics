def f(detector):
    people_in = 0
    for i in detector:
        if i == "+":
            people_in += 1
            if people_in == 3:
                return True
        elif i == "-":
            people_in -= 1
    return False

print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))
         
