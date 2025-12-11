pracownicy = [
    ("Smith", "Lucy"),
    ("Jones", "Janet"),
    ("Lee", "Jerry"),
    ("Jackson", "Peter"),
    ("Johnson", "Rick"),
    ("Lewis", "Terry"),
    ("Clarke", "Robin")
]

lista_sformatowana = list(map(
    lambda x: f"{x[0].upper()}, {x[1]}",
    pracownicy
))

print("Lista sformatowanych pracowników (z map/lambda):")
for linia in lista_sformatowana:
    print(linia)