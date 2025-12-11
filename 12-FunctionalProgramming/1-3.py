def ms_to_kmh(ms):
    return ms * 3.6

ms1 = int(input("Enter ms to convert "))

result = ms_to_kmh(ms1)

print(f"{ms1} to kmh is {result} ")