import json

def f(city_name):
    with open ("data.json", "r", encoding = 'utf-8') as file:
        data = json.load(file)
    count = 0
    total_age = 0
    for person in data:
        if person['city'] == city_name:
            count += 1
            total_age += person['age']
    if count == 0:
        return 0
    return total_age/count
    