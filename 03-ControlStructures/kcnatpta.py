###
# A program for checking clothing sizes
# S: Small size, M: Medium size, L: Large size
# XL: Extra large size or Incorrect symbol (if entered symbol
# dirrerent than S, M, L, XL)
#
# size = input('Enter size symbol: ')

# if size == 'S':
#     print('S: Small size')
# elif size == 'M':
#     print("M: size medium")
# else:
#     print("L - size large




###
# Checking whether the number
# entered from the keyboard is even or odd 
#
# number = int(input('Enter number: '))

# if number % 2 == 0:
#     print(f'{...} is even')
# else:
#     print(f'{...} is odd')



###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
bonus = 0.15 # 15%
is_bonus = input('do you got bonus (y/n) ') 

if is_bonus == "y":
    total_salary = basic_salary*bonus + basic_salary
else:
    basic_salary

print(f'Bonus included? {total_salary}')