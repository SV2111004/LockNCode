def normalize_text(text):
    """Remove spaces and make text uppercase."""
    return ''.join(filter(str.isalpha, text.upper()))


def encrypt(text, rails):
    text = normalize_text(text)
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in text:
        fence[rail].append(char)
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1

    return ''.join([''.join(row) for row in fence])


def decrypt(cipher, rails):
    cipher = normalize_text(cipher)
    pattern = list(range(rails)) + list(range(rails - 2, 0, -1))
    indexes = [pattern[i % len(pattern)] for i in range(len(cipher))]
    rail_len = [indexes.count(r) for r in range(rails)]
    rails_content = []
    i = 0
    for r_len in rail_len:
        rails_content.append(list(cipher[i:i + r_len]))
        i += r_len

    result = []
    rail_indices = [0] * rails
    for r in indexes:
        result.append(rails_content[r][rail_indices[r]])
        rail_indices[r] += 1

    return ''.join(result)


def process(text, rails, action):
    if action == "Encrypt":
        return encrypt(text, rails)
    else:
        return decrypt(text, rails)


if __name__ == "__main__":
    text = input("Enter text: ")
    rails = int(input("Enter rail depth: "))
    action = input("Encrypt or Decrypt? ").capitalize()

    result = process(text, rails, action)
    print(f"\nResult: {result}")
