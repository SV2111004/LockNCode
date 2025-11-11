def normalize(text):
    return ''.join(text.upper().split())

def encrypt(text, key):
    text = normalize(text)
    key = normalize(key)
    cipher = ""
    for i, char in enumerate(text):
        shift = ord(key[i % len(key)]) - 65
        cipher += chr((ord(char) - 65 + shift) % 26 + 65)
    return cipher

def decrypt(cipher, key):
    cipher = normalize(cipher)
    key = normalize(key)
    plain = ""
    for i, char in enumerate(cipher):
        shift = ord(key[i % len(key)]) - 65
        plain += chr((ord(char) - 65 - shift) % 26 + 65)
    return plain
