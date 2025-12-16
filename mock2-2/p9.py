import csv

def f(department_name):
    with open("data.csv", "r", encoding="utf-8") as file:
        data = csv.DictReader(file)
        count = 0
        for row in data:
            if row["Dział"] == department_name:
                count += 1
        return count



