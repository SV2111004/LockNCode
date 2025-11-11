import math

# ---------- Helper Functions ----------

def gcd(a, b):
    """Return Greatest Common Divisor using Euclid’s Algorithm."""
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(e, phi):
    """Compute modular inverse of e under modulo phi using Extended Euclid Algorithm."""
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = egcd(b % a, a)
            return (g, x - (b // a) * y, y)
    g, x, _ = egcd(e, phi)
    if g != 1:
        return None
    return (x + phi) % phi  # ensures positive modular inverse


# ---------- RSA Encryption & Decryption ----------

def encrypt_number(m, e, n):
    """
    Encrypt a numeric message using RSA formula:
    c = (m^e) mod n
    """
    m = int(m)
    if m <= 0 or m >= n:
        raise ValueError("Message must be between 1 and n-1.")
    return pow(m, e, n)


def decrypt_number(c, d, n):
    """
    Decrypt a numeric cipher using RSA formula:
    m = (c^d) mod n
    """
    c = int(c)
    if c <= 0 or c >= n:
        raise ValueError("Cipher must be between 1 and n-1.")
    return pow(c, d, n)
