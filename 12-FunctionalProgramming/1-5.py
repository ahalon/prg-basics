def avg_speed(distance,hours,minutes):
    return distance / (hours + minutes/60)

dis = int(input("Enter distance: "))
hou = int(input("Enter hours: "))
min = int(input("Enter minutes: "))

result = avg_speed(dis, hou, min)
print(result)