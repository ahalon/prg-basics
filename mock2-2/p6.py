def f(expression):
    tokens = expression.spli()
    stack = []

    for token in tokens:
        if token.isdigit():
            stack.append(token)
        else:
            b = stack.pop
     