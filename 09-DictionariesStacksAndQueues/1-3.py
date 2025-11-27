## Zadanie 3: Słownik opisujący telefon i jego iteracja

# 1. Tworzenie słownika 'mobile' z 6 parami klucz-wartość
mobile = {
    "OS": "Android",
    "Model": "Galaxy S23",
    "RAM_GB": 8,
    "Storage_GB": 256,
    "Kolor": "Czarny",
    "Cena_PLN": 3999.99
}


# Iteracja przez klucze i wartości
for key, value in mobile.items():
    # Formatowanie wyświetlania zgodnie z przykładem
    print(f"{key}: {value}")
