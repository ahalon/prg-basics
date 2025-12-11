def f(subjects):
    return max(subjects, key=lambda sub: sum(subjects[sub])/len(subjects[sub]))

# Test
print(f({"math":[3,4,4], "geo":[5,4,4,4], "comp":[5,4]}))  # "comp"
