seven_wonders = [
    "Great Wall of China",
    "Petra",
    "Christ the Redeemer",
    "Machu Picchu",
    "Chichen Itza",
    "Roman Colosseum",
    "Taj Mahal"
]

file_name = 'seven_wonders_original.txt' 



print(f"Zapisuję do pliku {file_name} z zachowaniem oryginalnej kolejności...")


with open(file_name, 'w') as file:
    
    for item in seven_wonders:
        file.write(item + '\n')

print("Zapis zakończony.")

