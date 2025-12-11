# names = [
#    'James',
#    'Emily',
#    'William',
#    'Olivia',
#    'Benjamin',
#    'Sophia',
#    'Henry']

# sort_names = sorted(names, key=len)

# for i in sort_names:
#     print(i)

names = [
    'James',
    'Emily',
    'William',
    'Olivia',
    'Benjamin',
    'Sophia',
    'Henry']

sort_names_by_second_letter = sorted(names, key=lambda x: x[1])

for i in sort_names_by_second_letter:
    print(i)