def occurs(number, array):
    for value in array:
        if value == number:
            return True
    return False

arr = [15, 38, 7, 23, 14]

num = int(input("Number: "))
print("Array:", *arr)

if occurs(num, arr):
    print(f"Result: number {num} appears in the array")
else:
    print(f"Result: number {num} does NOT appear in the array")
