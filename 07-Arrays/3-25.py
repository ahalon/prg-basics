import matplotlib.pyplot as plt

x = []
y = []

# create x values
for n in range(-100, 101):
    x.append(n)  # dodajemy kolejne wartości x

# create y values
for n in x:
    y.append(n**2 - 3)  # y = x^2 - 3

# print chart
plt.plot(x, y)           # rysujemy linię wykresu
plt.title("Wykres f(x) = x^2 - 3")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)           # włączamy siatkę
plt.show()               # pokazujemy wykres
