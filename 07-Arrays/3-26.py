import matplotlib.pyplot as plt
import math

# lista kątów w stopniach
x_degrees = list(range(0, 361))
# konwersja na radiany i obliczenie sin(x)
y = [math.sin(math.radians(angle)) for angle in x_degrees]

# rysowanie wykresu
plt.plot(x_degrees, y)
plt.title("Wykres funkcji y = sin(x)")
plt.xlabel("Kąt (stopnie)")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()
