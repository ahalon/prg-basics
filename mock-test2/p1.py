cards = {
    'A': 10,
    'K' : 10,
    'Q' : 10,
    'J' : 10,
    'T' : 10,
    '9' : 9,
    '8' : 8,
    '7' : 7,
    '6' : 6,
    '5' : 5,
    '4' : 4,
    '3' : 3,
    '2' : 2,
    }

def f(player1, player2):

    s1 = sum(cards[c] for c in player1)

    s2 = sum(cards[c] for c in player2)

    return s1 >= s2

print(f("AJ972","AQT72"))
print(f("9532","K8"))


