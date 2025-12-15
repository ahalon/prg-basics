import json

def f(years, course, average_grade):
    with open ("data.json", "r") as file:
        data = json.load(file)

        
