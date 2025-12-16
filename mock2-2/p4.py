import re

def f(text):
    pattern = r'\b[a-zA-Z0-9.-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}\b'
    return len(re.findall(pattern, text))


# test
print(f("Kontakt: user@domena.pl i inny.email-123@sub.com. Zły_adres@"))
