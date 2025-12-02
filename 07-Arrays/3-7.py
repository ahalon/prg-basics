arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

i = 1

longest_name = arr[0]

while i < len(arr):
    if len(arr[i]) > len(longest_name):
        longest_name = arr[i]
    i += 1

print(f'longest name: {longest_name}')