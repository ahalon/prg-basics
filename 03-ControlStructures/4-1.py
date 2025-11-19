university = 'Krakow University of Economics'
university_expanded = ''

# Używamy pętli for do iteracji przez każdy znak (litera) w napisie 'university'
for char in university:
    # Do zmiennej 'university_expanded' dodajemy bieżący znak
    university_expanded += char
    # Następnie dodajemy spację po każdym znaku
    university_expanded += ' '

# Usuwamy dodatkową spację na końcu, która została dodana w ostatniej iteracji pętli
university_expanded = university_expanded.strip()

print(university_expanded)