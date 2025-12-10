# Inicjalizujemy pusty słownik, który będzie przechowywał mapowanie Litera -> Województwo
provinces = {}

# Otwieramy plik 'province.csv' do odczytu ('r') z kodowaniem UTF-8
with open("province.csv", "r", encoding="utf-8") as f:
    next(f)  # Pomijamy pierwszą linię, która jest nagłówkiem ('Letter,Name')
    
    # Przechodzimy przez każdą pozostałą linię w pliku
    for line in f:
        line = line.strip()  # Usuwamy białe znaki (np. znak nowej linii) z początku i końca linii
        
        # Sprawdzamy, czy linia nie jest pusta (jeśli pusta, przechodzimy do następnej iteracji)
        if not line:
            continue
            
        # Dzielimy linię na dwie części (literę i nazwę) używając przecinka jako separatora
        letter, name = line.split(",")
        
        # Dodajemy wpis do słownika: kluczem jest litera, wartością jest nazwa województwa
        provinces[letter] = name

# Inicjalizujemy słownik liczników, gdzie każdemu województwu przypisujemy wartość początkową 0
# Używamy do tego list comprehension (słownikowej), co jest szybkie i zwięzłe
counts = {name: 0 for name in provinces.values()}

# Otwieramy plik 'vehicle.txt' (z listą rejestracji) do odczytu
with open("vehicle.txt", "r", encoding="utf-8") as f:
    # Przechodzimy przez każdą linię (rejestrację) w pliku
    for line in f:
        reg = line.strip()  # Usuwamy białe znaki z rejestracji
        
        # Sprawdzamy, czy linia nie jest pusta
        if not reg:
            continue
            
        # Pobieramy pierwszy znak rejestracji i konwertujemy go na wielką literę
        first_letter = reg[0].upper()
        
        # Sprawdzamy, czy ta pierwsza litera jest kluczem w naszym słowniku provinces
        if first_letter in provinces:
            # Jeśli jest, pobieramy pełną nazwę województwa
            province_name = provinces[first_letter]
            
            # Zwiększamy licznik pojazdów dla tego konkretnego województwa o 1
            counts[province_name] += 1

# --- Drukowanie Wyników ---
# Przechodzimy przez słownik z wynikami (klucz: województwo, wartość: liczba pojazdów)
for province, num in counts.items():
    # Formatujemy i drukujemy wynik w postaci np. "Dolnośląskie: 5"
    print(f"{province}: {num}")
