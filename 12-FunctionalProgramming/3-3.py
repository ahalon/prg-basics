stock = [
    (20, 5.50), 
    (15, 8.30),
    (37, 3.85),
    (4, 11.60)
]

wartosci_poszczegolnych_pozycji = map(lambda x: x[0] * x[1], stock)

wartosc_calkowita = sum(wartosci_poszczegolnych_pozycji)

print(f"Całkowita wartość zapasów: {wartosc_calkowita:.2f} PLN")
