def tlumacz_slownik():
    # 1. Nasz słownik tłumaczeń
    translations = {
       'computer': 'komputer',
       'mouse': 'myszka',
       'keyboard': 'klawiatura',
       'printer': 'drukarka',
       'monitor': 'monitor' # Dorzuciłem dla lepszego przykładu
    }

    # 2. Pobieramy słowo od użytkownika
    # Zmieniamy na małe litery (lower()), żeby uniknąć problemów z wielkością liter.
    slowo_ang = input("Podaj angielskie słowo do przetłumaczenia: ").lower().strip()

    # 3. Szukamy tłumaczenia
    # Używamy metody .get() dla bezpieczeństwa, żeby program się nie wykrzaczył.
    # Jeśli słowa (klucza) nie ma w słowniku, .get() zwróci domyślny komunikat.
    
    tlumaczenie = translations.get(slowo_ang)

    if tlumaczenie:
        # Tłumaczenie znalezione (klucz był w słowniku)
        print(f"✔️ Tłumaczenie dla '{slowo_ang}' to: **{tlumaczenie}**")
    else:
        # Tłumaczenie nie znalezione (klucz nie był w słowniku)
        print(f"❌ Przepraszam, tłumaczenie słowa '{slowo_ang}' jest niedostępne w tej bazie.")

# Uruchomienie funkcji
tlumacz_slownik()