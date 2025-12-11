people = [
    {'name': 'John', 'age' : 24},
    {'name': 'Ann', 'age' : 19},
    {'name': 'Peter', 'age' : 31}
]

posortowani_wiekiem = sorted(people, key=lambda x: x['age'])

for person in posortowani_wiekiem:
    print(f"{person['name']}: {person['age']}")