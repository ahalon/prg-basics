def f(n):
    count = 0  # ile liczb pierwszych znaleziono
    num = 2    # zaczynamy od pierwszej liczby pierwszej

    while True:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:  # jeśli dzieli się przez coś poza 1 i samą siebie
                is_prime = False
                break

        if is_prime:  # jeśli liczba jest pierwsza
            count += 1
            if count == n:  # jeśli to n-ta liczba pierwsza
                return num

        num += 1  # sprawdzamy kolejną liczbę

# testy
print(f(1))  # 2
print(f(5))  # 11
print(f(10)) # 29