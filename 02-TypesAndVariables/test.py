university = "Krakow University of Economics"

# 1. Dzieli ciąg na listę słów
words = university.split()

# 2. Tworzy listę pierwszych liter, zmieniając je na wielkie
abbreviation_letters = [word[0].upper() for word in words]

# 3. Łączy litery w jeden ciąg znaków
abbreviation = "".join(abbreviation_letters)

# 4. Drukuje wynik
print(abbreviation)