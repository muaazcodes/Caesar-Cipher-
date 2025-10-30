import alphabet

def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char.upper() in alphabet.alphabet:
            position = alphabet.alphabet.index(char.upper())
            new_position = (position + shift_key) % 26
            cipher_text += alphabet.alphabet[new_position]
        else:
            cipher_text += char
        print(f"Here is the text after encryption: {cipher_text}")
    

def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char.upper() in alphabet.alphabet:
            position = alphabet.alphabet.index(char.upper())
            new_position = (position - shift_key) % 26
            plain_text += alphabet.alphabet[new_position]
        else:
            plain_text += char
    print(f"Here is the text after decryption: {plain_text}")
    

# ---- main program (run only if executed directly) ----
if __name__ == "__main__":
    what_do = input("Type encrypt for encryption or decrypt for decryption:\n").lower()
    text = input("Type your message:\n").upper()
    shift = int(input("Enter shift key:\n"))

    if what_do == "encrypt":
        encryption(plain_text=text, shift_key=shift)
    elif what_do == "decrypt":
        decryption(cipher_text=text, shift_key=shift)
    else:
        print("Invalid choice.")
