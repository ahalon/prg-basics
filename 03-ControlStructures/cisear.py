plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    
    code = ord(char)
 
    code += 1


    new_char = chr(code)

    encrypted_text += new_char

print("Plain text:", plain_text)
print("Encrypted text:", encrypted_text)
