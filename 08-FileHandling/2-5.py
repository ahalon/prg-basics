shopping_list = 'shopping_list.txt'

# --- Funkcja dodająca produkt na koniec listy zakupów ---
def add_product(file_name, product_name):
    # Otwieramy plik w trybie dopisywania ('a')
    with open(file_name, 'a') as file:
        # Zapisujemy nazwę produktu, dodając '\n' dla nowej linii
        file.write(product_name + '\n')

# --- Główna pętla pobierająca dane ---
product = ""
while product != '0':
    # Pobieramy produkt od użytkownika
    product = input('Enter product name (0 stops): ')
    
    if product == '0':
        # Jeśli użytkownik wpisze '0', pętla 'while' automatycznie się zakończy.
        # Możemy tutaj opuścić klauzulę 'if', ale w celu zachowania struktury:
        print("Zapisywanie zakończone.")
        break
    else:
        # Jeśli wpisano produkt, dodajemy go do pliku
        add_product(shopping_list, product)