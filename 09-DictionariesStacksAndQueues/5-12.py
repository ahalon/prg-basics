# 1. Pobierz tekst od użytkownika
text_to_reverse = input("Podaj tekst, a ja go odwrócę: ")

# 2. Inicjalizacja Stosu (lista)
stack = []

# 3. Pchaj (Push) każdy znak na stos
for char in text_to_reverse:
    stack.append(char)

# 4. Inicjalizacja pustego stringa na wynik
reversed_text = ""

# 5. Wyciągaj (Pop) znaki ze stosu i łącz je
while stack:
    reversed_text += stack.pop()

# 6. Wypisz wynik
print(f"\nStary tekst: **{text_to_reverse}**")
print(f"Nowy tekst (odwrócony): **{reversed_text}**")