import csv

def f(value):
    count = 0
    with open("data.csv", "r", encoding="utf8") as file:
        data = list(csv.DictReader(file))
        for worker in data:
            if float(worker["salary"]) >= value:
                count += 1
    return count
