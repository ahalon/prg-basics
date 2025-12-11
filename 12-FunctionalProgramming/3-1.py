arr = [
    15.90,
    38.47,
    4.07,
    132.70,
    9.15
]

# print(list(map(lambda x: round(x * 4.5), arr)))

wynik = [(x*4.5) for x in arr]

print(wynik)
