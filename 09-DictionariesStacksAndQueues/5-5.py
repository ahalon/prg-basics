paragraph = "cat dog mouse cat rat cat mouse"

splited = paragraph.split()

licznik_slow = {}

for i in splited:
    if i in licznik_slow:
        licznik_slow[i] += 1
    else:
        licznik_slow[i] = 1

print(licznik_slow)    