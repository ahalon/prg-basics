# with open ("story.txt", "r") as file:
#     text = file.read()
#     words = text.split()

# print(len(words))
# print(sorted(words, key=len, reverse = True))[:5]



# #skopiuj zawartość a.txt do b.txt każdą linię zapisz wielkimi literami
# with open("a.txt", "r") as source_file, open("b.txt", "w") as target_file:
#     for line in source_file:
#         target_file.write(line.upper())

# #użytkownik podaje nazwę pliku; 
# # jeśli plik nie istnieje → wypisz komunikat; 
# # jeśli istnieje → wypisz liczbę znaków

# nazwa = input("Podaj nazwe pliku: ")

# try:
#     with open (nazwa, "r") as file:
#         text = file.read()
#         liczba_znakow = len(text)
# except FileNotFoundError:
#     print("Plik nie istnieje.")


# #otwórz plik numbers.txt
# #wypisuj 3 linie naraz
# #po każdej trójce: Press Enter...

# with open ("numbers.txt" "r") as file:
#     for line in file:

def f(first_letter,last_letter):
    with open ("data.txt", "r") as file:
        text = file.read()
        words = text.split()
    count = 0 
    for word in words:
        if word.startswith(first_letter) and word.endswith(last_letter):
            count += word
    return count
