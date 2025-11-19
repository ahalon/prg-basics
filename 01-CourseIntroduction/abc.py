# name = "Ann"
# print(name)
# print(f"My name is {name}")

# age = int(input("Your age: "))

# if age > 18:
#     print("You are an adult")
# else:
#     print("You are a child")

while True:
        try:
        
            wiek_str = input("Podaj swój wiek: ")

            # 2. Próba konwersji (potencjalne miejsce błędu)
            wiek_int = int(wiek_str)

            # 3. Jeśli konwersja się udała, wychodzimy z pętli
            break

        except ValueError:
        # 4. Obsługa błędu, jeśli int() nie może skonwertować tekstu
            print("\n❌ Niepoprawne dane! Wiek musi być podany jako liczba całkowita.")
            print("   Spróbuj raz jeszcze.\n")


# Kod poza pętlą wykonuje się tylko, gdy dane są poprawne
print(f"\n✅ Dziękuję! Twój wiek to {wiek_int} lat.")