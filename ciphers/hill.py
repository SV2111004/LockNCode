import numpy as np

def normalize(text):
    return ''.join(text.upper().split())

def encrypt(text, key_matrix):
    text = normalize(text)
    n = key_matrix.shape[0]
    while len(text) % n != 0:
        text += 'X'
    cipher = ''
    for i in range(0, len(text), n):
        block = np.array([ord(c) - 65 for c in text[i:i+n]])
        enc = np.dot(key_matrix, block) % 26
        cipher += ''.join(chr(num + 65) for num in enc)
    return cipher

def decrypt(cipher, key_matrix):
    cipher = normalize(cipher)
    n = key_matrix.shape[0]
    det = int(round(np.linalg.det(key_matrix))) % 26
    inv_det = pow(det, -1, 26)
    adj = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
    inv_key = (inv_det * adj) % 26
    plain = ''
    for i in range(0, len(cipher), n):
        block = np.array([ord(c) - 65 for c in cipher[i:i+n]])
        dec = np.dot(inv_key, block) % 26
        plain += ''.join(chr(num + 65) for num in dec)
    return plain
