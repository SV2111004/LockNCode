import string
def normalize(text):
    return ''.join(text.upper().split())

def encrypt(text, key):
    text = normalize(text)
    alpha = string.ascii_uppercase
    table = str.maketrans(alpha, key.upper())
    return text.translate(table)

def decrypt(cipher, key):
    cipher = normalize(cipher)
    alpha = string.ascii_uppercase
    table = str.maketrans(key.upper(), alpha)
    return cipher.translate(table)
