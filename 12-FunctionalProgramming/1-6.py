speed = lambda x, y, z: x / (y + z/60)

x = int(input("Enter distance: "))
y = int(input("Enter hours: "))
z = int(input("Enter minutes: "))

result = speed(x, y, z)
print(result)