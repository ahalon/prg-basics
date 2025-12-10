winter_semester = {
   "math":60,
   "programming":30,
   "history":15
}

liczba_godzin = 0

for value in winter_semester.values():
    liczba_godzin += value

print(f"liczba godzin w semestrze wynosi: {liczba_godzin}")