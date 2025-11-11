def normalize(text):
    return ''.join(text.upper().split())

def encrypt(text, key):
    text = normalize(text)
    columns = [''] * key
    for i, char in enumerate(text):
        columns[i % key] += char
    return ''.join(columns)

def decrypt(cipher, key):
    cipher = normalize(cipher)
    num_rows = len(cipher) // key
    extra = len(cipher) % key
    rows = []
    index = 0
    for i in range(key):
        length = num_rows + (1 if i < extra else 0)
        rows.append(cipher[index:index+length])
        index += length
    result = ''
    for i in range(num_rows + 1):
        for row in rows:
            if i < len(row):
                result += row[i]
    return result
