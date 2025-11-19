plain_text = "Ala ma kota"
encrypted_text = ""
codes = [ord(char) for char in plain_text]
codes = [c + 1 for c in codes]
codes = [chr(c) for c in codes]
encrypted_text = "".join(c for c in codes)

print(encrypted_text)