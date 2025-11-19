total_tasks = 20
tasks_ok = int(input("Number of correct tasks: "))
test_passed = False

if tasks_ok / total_tasks >= 0.5 :
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')



###
# Checking whether the number
# entered from the keyboard is even or odd 
#
number = int(input('Enter number: '))

if number % 2 = 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')


###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
bonus = 0.15 # 15%
is_bonus = input('Does the employee receive a bonus? (Y/N):') == 'Y'

if is_bonus:
    total_salary = basic_salary + 0.15 * basic_salary
else:
    total_salary == basic_salary

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {basic_salary+bonus}')