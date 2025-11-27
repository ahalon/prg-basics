# Słownik początkowy (zgodny z przykładem)
person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming", "excursions"],
    "married": True,
    "phone": {"landline": "123444321", "mobile": "777888999"}
}

print("\n--- OPERACJE NA SŁOWNIKU ---")

# i. Wyświetla imię
print("i. Imię:", person["name"])

# ii. Wyświetla hobby
print("ii. Hobby:", person["hobby"])

# iii. Wyświetla całą zawartość słownika
print("iii. Cała zawartość (przed zmianami):", person)

# iv. Zmienia nazwisko na 'Nowak'
person["surname"] = "Nowak"
print("iv. Nazwisko zmienione na:", person["surname"])

# v. Zmienia status małżeński (z True na False lub odwrotnie)
person["married"] = not person["married"] # not True daje False
print("v. Status małżeński zmieniony na:", person["married"])

# vi. Dodaje płeć: 'male'
person["gender"] = "male"
print("vi. Dodano płeć:", person["gender"])

# vii. Dodaje nowe hobby: 'bicycle'
person["hobby"].append("bicycle")
print("vii. Nowa lista hobby:", person["hobby"])

# viii. Dodaje telefon służbowy do istniejących telefonów
# Zmieniamy wewnętrzny słownik 'phone'
person["phone"]["work"] = "313131444"
print("viii. Dodano telefon służbowy:", person["phone"]["work"])

# ix. Wyświetla całą zawartość słownika (iteracja)
print("\nix. Cała zawartość po zmianach (iteracja):")
for key, value in person.items():
    print(f"   {key}: {value}")

print("----------------------------")