###
# A program for checking clothing sizes
# S: Small size, M: Medium size, L: Large size
# XL: Extra large size or Incorrect symbol (if entered symbol
# dirrerent than S, M, L, XL)
#
size = input('Enter size symbol: ')

if size == 'S':
    print('S: Small size')
elif size == 'M':
    print("Medium size")
elif size == "L":
    print("Large size")
else:
    print("XL size")


###
# The car has three driving modes: Auto (A), Manual (M) and Eco (E).
# In each of these three modes, the average fuel consumption in liters
# per 100 km is 7, 9 and 6 respectively. Write a program that calculates
# total fuel consumption for a given distance in km and a given
# driving mode.
#
driving_mode = input('Enter driving mode (A/M/E):')
distance = int(input('Enter distance in km'))

if driving_mode == 'A':
    fuel_consumption = 7 # liters per 100km
elif driving_mode == 'M':
    fuel_consumption = 8
else:
    fuel_consumption = 9

total_consumption = fuel_consumption
print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')


###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = int(input("enter first number: "))
number2 = int(input("enter first number: "))
operator = input("Operator: ")

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
else:
    result = number1/number2

# print result
print(f'{number1} {operator} {number2} = {result}')




###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1..12): '))

if month >= 10:
    quarter = 4
elif ...:
    ...

print('Month {...} is in quarter {...}')

# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1..12): '))

# Pamiętaj, że kwartały to:
# I kwartał: miesiące 1, 2, 3
# II kwartał: miesiące 4, 5, 6
# III kwartał: miesiące 7, 8, 9
# IV kwartał: miesiące 10, 11, 12

if month >= 10:
    quarter = 4
elif month >= 7:
    quarter = 3
elif month >= 4:
    quarter = 2
else:
    quarter = 1

if quarter:
    print(f'Month {month} is in quarter {quarter}')
else:
    print('Error: Invalid month number entered.')



###
# Checking login and password
#
login = 'joe'
password = 'abcd'
entered_login = input('Login: joe')
entered_password = input('Password: abcd')
if login == entered_login and entered_password :
    print('You are logged in')
else:
    print('Incorrect login or password!!')