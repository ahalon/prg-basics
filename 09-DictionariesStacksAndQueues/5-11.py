import json
import os

# sprawdzamy czy plik istnieje; jeśli nie, tworzymy pusty słownik
if os.path.exists("voting.json"):
    with open("voting.json", "r", encoding="utf-8") as f:
        try:
            votes = json.load(f)
        except json.JSONDecodeError:
            votes = {}
else:
    votes = {}

# głosowanie
person_name = input("Name of the person you are voting for: ").strip()

if person_name in votes:
    votes[person_name] += 1
else:
    votes[person_name] = 1

# zapis wyników
with open("voting.json", "w", encoding="utf-8") as f:
    json.dump(votes, f, indent=4, ensure_ascii=False)

print("Vote recorded.")
