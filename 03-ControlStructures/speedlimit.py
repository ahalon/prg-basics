###
# Checking whether a car exceeded the speed limit
#
speed_limit = 140
car_speed = int( input('Enter car speed (km/h): ') )

if car_speed >140:
    print(f'Your speed is {car_speed}km/h')
    print('Warning: speed limit exceeded!!')


###
# Credit card payment 
#
account_balance = 500
total_payment = int(input("Total cost is"))

if total_payment > account_balance:
    print('Payment completed')
else:
    print('No funds')


###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#
total_tasks = 20
tasks_ok = int(input("Number of correct tasks: "))
test_passed = False

if tasks_ok / total_tasks >= 0.5 :
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')
