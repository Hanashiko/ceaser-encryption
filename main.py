def caesar_cipher(text):
    alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    encrypted_text = ""
    
    for char in text:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            shifted_index = (index + 2) % len(alphabet)
            encrypted_char = alphabet[shifted_index]
            if char.isupper():
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

plaintext = input().lower()
ciphertext = caesar_cipher(plaintext)
print(f"Encrypted text: {ciphertext}")
