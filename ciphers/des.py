from pyDes import des, PAD_PKCS5
import base64

def normalize(text):
    """Remove extra spaces and convert to uppercase."""
    return text.strip().upper()

def encrypt(text, key):
    """
    Encrypt text using DES (Data Encryption Standard).
    Key must be exactly 8 characters long.
    """
    text = normalize(text)
    key = (key[:8] + "ABCDEFGH")[:8]  # ensure key is 8 characters
    k = des(key, padmode=PAD_PKCS5)
    encrypted = k.encrypt(text.encode())
    return base64.b64encode(encrypted).decode()

def decrypt(cipher, key):
    """
    Decrypt text encrypted by DES.
    """
    key = (key[:8] + "ABCDEFGH")[:8]
    k = des(key, padmode=PAD_PKCS5)
    try:
        decrypted = k.decrypt(base64.b64decode(cipher))
        return decrypted.decode().upper()
    except Exception:
        return "❌ Decryption Failed: Invalid key or ciphertext"
