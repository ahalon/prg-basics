oceny = [3.0, 5.0, 2.0, 3.5, 4.0, 4.0, 3.5, 2.0, 4.0, 2.0]


dobre_oceny = list(filter(lambda x: x != 2.0, oceny))

srednia = sum(dobre_oceny) / len(dobre_oceny)

print(f'Srednia to {round(srednia, 2)}')