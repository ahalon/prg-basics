# f = open("")
# data = f.read()
# print(data)
# f.close()
# with open ('countries.txt' , 'r')  as file:
#      content = file.readlines()
#      posortowane = sorted(content)
#      for i, line in enumerate(posortowane):
#          print(f'{i+1}. {line.strip()}')


# def read_from_file(name):
#    with open(name) as file:
#       content = file.read()
#    return content

# # reads the entire file and splits lines into array
# file_content = read_from_file('car_park.txt')
# file_lines = file_content.splitlines()

# # calculates the total number of cars parked
# total = 0
# for line in file_lines:
#    total += int(line)
# print(f'Total cars parked:{total}')

# --- Funkcja pomocnicza ---
# def read_from_file(name):
#     """Odczytuje całą zawartość pliku i zwraca jako pojedynczy ciąg znaków."""
#     with open(name, 'r') as file:
#         return file.read()



# pets_text = read_from_file('pets.txt')

# print("--- ZADANIE 8: Analiza pliku pets.txt ---")
# print("=== Zawartość pliku ===")


# print(pets_text)


# word_list = pets_text.split()


# word_count = len(word_list)

# print("=========================")
# print(f"Całkowita liczba słów w tekście: {word_count}")

file_name = 'it_company.csv'
job_title = 'Software Engineer'
counter = 0

with open(file_name, 'r') as file:
    print(f"Pracownicy na stanowisku: {job_title}")
    
    for line in file:
        if job_title in line:
            counter += 1
            
            
            print(f"{counter}. {line.strip()}")