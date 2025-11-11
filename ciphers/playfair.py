import string

def normalize(text):
    """Uppercase, remove non-alpha, replace J with I."""
    return ''.join([c for c in text.upper() if c.isalpha()]).replace('J', 'I')

def generate_matrix(key):
    """
    Build 5x5 Playfair matrix from key.
    J is merged into I.
    """
    key = normalize(key)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # note: J omitted
    seen = []
    for ch in key + alphabet:
        if ch not in seen:
            seen.append(ch)
    # return 5x5 list-of-lists
    return [seen[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, ch):
    """Return (row, col) of ch in matrix."""
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c
    raise ValueError(f"Character {ch} not in matrix")

def make_pairs(text):
    """
    Convert normalized text into digraphs per Playfair rules:
    - split into pairs
    - if pair letters are equal, insert 'X' after first and re-pair
    - pad final single with 'X'
    """
    text = normalize(text)
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else None
        if b is None:
            # last single char -> pad with X
            pairs.append(a + 'X')
            i += 1
        elif a == b:
            # double letter -> aX, move only one step
            pairs.append(a + 'X')
            i += 1
        else:
            pairs.append(a + b)
            i += 2
    return pairs

def encrypt(plaintext, key):
    """
    Encrypt plaintext with Playfair using key.
    Returns ciphertext (uppercase, no spaces).
    """
    matrix = generate_matrix(key)
    pairs = make_pairs(plaintext)
    cipher = []
    for pair in pairs:
        a, b = pair[0], pair[1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:
            # same row -> shift right
            cipher.append(matrix[r1][(c1 + 1) % 5])
            cipher.append(matrix[r2][(c2 + 1) % 5])
        elif c1 == c2:
            # same column -> shift down
            cipher.append(matrix[(r1 + 1) % 5][c1])
            cipher.append(matrix[(r2 + 1) % 5][c2])
        else:
            # rectangle -> swap columns
            cipher.append(matrix[r1][c2])
            cipher.append(matrix[r2][c1])
    return ''.join(cipher)

def decrypt(ciphertext, key):
    """
    Decrypt ciphertext (assumes valid even-length ciphertext).
    Returns plaintext with inserted 'X' possibly present; we attempt to remove padding Xs
    that were added during encryption: remove trailing X if it was padding.
    Note: removal of internal filler Xs is heuristic — manual review may be needed.
    """
    matrix = generate_matrix(key)
    # normalize ciphertext (keep only letters, uppercase, J->I not required here)
    cipher = ''.join([c for c in ciphertext.upper() if c.isalpha()])
    if len(cipher) % 2 != 0:
        raise ValueError("Ciphertext length should be even for Playfair")

    pairs = [cipher[i:i+2] for i in range(0, len(cipher), 2)]
    plain = []
    for pair in pairs:
        a, b = pair[0], pair[1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:
            # same row -> shift left
            plain.append(matrix[r1][(c1 - 1) % 5])
            plain.append(matrix[r2][(c2 - 1) % 5])
        elif c1 == c2:
            # same column -> shift up
            plain.append(matrix[(r1 - 1) % 5][c1])
            plain.append(matrix[(r2 - 1) % 5][c2])
        else:
            # rectangle -> swap columns
            plain.append(matrix[r1][c2])
            plain.append(matrix[r2][c1])

    # post-process: remove trailing 'X' if it was a padding
    plain_text = ''.join(plain)
    # if last char is 'X' and was added as padding, remove it
    if plain_text.endswith('X'):
        plain_text = plain_text[:-1]
    return plain_text
