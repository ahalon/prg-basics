def f(results):
    best_avg = 0
    best_student = None
    for student, grade in results.items():
        avg = sum(grade)/len(grade)
        if avg > best_avg:
            best_avg = avg
            best_student = student
    return best_student

print(f({"Anna": [4, 5, 3], "Piotr": [5, 5, 5], "Kasia": [4, 4, 5, 3]}))

