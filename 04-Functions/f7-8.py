def f(amount_to_pay):
    sum_coins = 0
    piatki = amount_to_pay // 5 
    to_pay = amount_to_pay % 5
    dwojki = to_pay // 2
    to_pay = to_pay % 2
    jedynki = to_pay // 1



    sum_coins += piatki
    sum_coins += dwojki
    sum_coins += jedynki

    return sum_coins

print(f(23))