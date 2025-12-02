import re

email_file = 'report.txt'
total_purchases = 0.0

# 1. Odczyt zawartości pliku (z poprawnym kodowaniem)
with open(email_file, 'r', encoding="utf-8") as file:
    email = file.read()

# 2. Wzorzec i ekstrakcja kwot (np. "12.50", "99,99")
# Wzorzec: jedna lub więcej cyfr, separator (kropka/przecinek), jedna lub więcej cyfr.
pattern = r'\d+[\.,]\d+' 
amounts_str = re.findall(pattern, email)

# 3. Sumowanie kwot
for amount_str in amounts_str:
    # Zamieniamy przecinki na kropki, aby Python mógł skonwertować na float
    cleaned_amount = amount_str.replace(',', '.')
    
    # Konwertujemy na float i dodajemy
    total_purchases += float(cleaned_amount)

# 4. Wydruk wyniku
print(f"Całkowita wartość wydatków: {total_purchases:.2f}")