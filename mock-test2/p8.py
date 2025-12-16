def f(expression):
    stack = []
    tokens = expression.split()   # rozbijamy wyrażenie na kawałki

    for token in tokens:
        if token.isdigit():       # jeśli liczba
            stack.append(int(token))
        else:                     # jeśli operator (+ lub -)
            b = stack.pop()       # bierzemy ostatnią liczbę
            a = stack.pop()       # bierzemy przedostatnią liczbę
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)

    return stack[0]               # na końcu stos ma tylko wynik
