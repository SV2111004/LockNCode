def normalize(text):
    return ''.join(text.upper().split())

def encrypt(text, shift):
    text = normalize(text)
    result = ""
    for char in text:
        if char.isalpha():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
    return result

def decrypt(cipher, shift):
    return encrypt(cipher, -shift)
