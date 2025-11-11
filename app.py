import streamlit as st
import numpy as np
from ciphers import (
    caesar, monoalphabetic, playfair, railfence, polyalphabetic,
    hill, rsa, transposition, des
)

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="🔐 LOCK N CODE",
    page_icon="🖤",
    layout="wide",
    initial_sidebar_state="expanded"
)
# ---------------------- CYBER STYLING ----------------------
st.markdown("""
<style>
/* Dark background */
body {
    background-color: #0f0f0f;
    color: #00ffea;
    font-family: 'Courier New', monospace;
}

/* Headings with subtle glow */
h1 {
    color: #00ffea;
    text-align: center;
    text-shadow: 0 0 3px #00ffea, 0 0 6px #00ffea;
}
h4 {
    color: #00c3ff;
    text-align: center;
    text-shadow: 0 0 2px #00c3ff, 0 0 4px #00c3ff;
}

/* Card style for all ciphers */
.card {
    padding: 20px;
    border-radius: 12px;
    background-color: #1a1a1a;
    border: 2px solid #00ffea;
    box-shadow: 0 0 10px rgba(0,255,234,0.3);
    margin-bottom: 20px;
}

/* Inputs */
input, textarea {
    background-color: #0f0f0f !important;
    color: #00ffea !important;
    border: 1px solid #00ffea !important;
    border-radius: 5px;
}

/* Buttons */
.stButton>button {
    background-color: #00c3ff;
    color: #000;
    font-weight: bold;
    border-radius: 8px;
}
.stButton>button:hover {
    background-color: #008bb5;
    color: #fff;
}

/* Terminal-style outputs */
.terminal {
    background-color: #000;
    color: #00ff00;
    padding: 10px;
    border-radius: 8px;
    font-family: 'Courier New', monospace;
    border: 1px solid #00ffea;
    word-wrap: break-word;
}
</style>
""", unsafe_allow_html=True)

# ---------------------- HEADER ----------------------
st.markdown("<h1>🔐 LOCK N CODE</h1>", unsafe_allow_html=True)
st.markdown("<h4>Cyber Encryption & Decryption Hub</h4>", unsafe_allow_html=True)
st.divider()

# ---------------------- SIDEBAR ----------------------
st.sidebar.title("⚙️ Cipher Selection")
cipher_choice = st.sidebar.selectbox(
    "Choose Cipher Method:",
    [
        "Caesar Cipher",
        "Monoalphabetic Cipher",
        "Playfair Cipher",
        "Rail Fence Cipher",
        "Polyalphabetic (Vigenère)",
        "Hill Cipher",
        "RSA Cipher",
        "Transposition Cipher",
        "DES Cipher"
    ]
)
mode = st.sidebar.radio("Mode:", ["Encrypt", "Decrypt"])
st.sidebar.markdown("---")
st.sidebar.markdown("© 2025 **LOCK N CODE** | Built with ❤️ Python & Streamlit")

# ---------------------- MAIN AREA ----------------------
st.subheader(f"🔹 {cipher_choice} | {mode}")

if cipher_choice != "RSA Cipher":
    text_input = st.text_area("Enter your text here:", placeholder="Type your message...", height=120)

# ---------------------- CIPHER LOGIC ----------------------
def run_cipher(func, *args):
    try:
        result = func(*args)
        st.markdown(f"<div class='terminal'>{result}</div>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error: {e}")

# ---------------------- CARD FUNCTION ----------------------
def card(title, description, inputs_func):
    with st.container():
        st.markdown(f"<div class='card'>### {title}</div>", unsafe_allow_html=True)
        st.write(description)
        inputs_func()

# ---------------------- CIPHER CARDS ----------------------

# Caesar Cipher
if cipher_choice == "Caesar Cipher":
    def inputs():
        key = st.number_input("Shift Value:", min_value=1, max_value=25, value=3)
        if st.button("Run Cipher"):
            run_cipher(caesar.encrypt if mode=="Encrypt" else caesar.decrypt, text_input, key)
    card("🥷 Caesar Cipher", "Shift each letter by a fixed number.", inputs)

# Monoalphabetic Cipher
elif cipher_choice == "Monoalphabetic Cipher":
    def inputs():
        key = st.text_input("26-letter Key:", placeholder="QWERTYUIOPASDFGHJKLZXCVBNM")
        if st.button("Run Cipher"):
            if len(key) != 26:
                st.error("Key must be 26 letters.")
            else:
                run_cipher(monoalphabetic.encrypt if mode=="Encrypt" else monoalphabetic.decrypt, text_input, key)
    card("🔤 Monoalphabetic Cipher", "Substitute each letter according to a key alphabet.", inputs)

# Playfair Cipher
elif cipher_choice == "Playfair Cipher":
    def inputs():
        key = st.text_input("Key Word:", placeholder="LOCKCODE")
        if st.button("Run Cipher"):
            run_cipher(playfair.encrypt if mode=="Encrypt" else playfair.decrypt, text_input, key)
    card("🔑 Playfair Cipher", "Encrypts digrams using a key square.", inputs)

# Rail Fence Cipher
elif cipher_choice == "Rail Fence Cipher":
    def inputs():
        rails = st.number_input("Rail Depth:", min_value=2, max_value=10, value=3)
        if st.button("Run Cipher"):
            run_cipher(railfence.encrypt if mode=="Encrypt" else railfence.decrypt, text_input, rails)
    card("🛤️ Rail Fence Cipher", "Zig-zag encryption using rails.", inputs)

# Vigenere Cipher
elif cipher_choice == "Polyalphabetic (Vigenère)":
    def inputs():
        key = st.text_input("Key Word:", placeholder="LOCKCODE")
        if st.button("Run Cipher"):
            run_cipher(polyalphabetic.encrypt if mode=="Encrypt" else polyalphabetic.decrypt, text_input, key)
    card("🔒 Vigenère Cipher", "Encrypt using repeating key letters.", inputs)

# Hill Cipher
elif cipher_choice == "Hill Cipher":
    def inputs():
        matrix_input = st.text_input("Square Matrix (e.g., [[3,3],[2,5]]):")
        if st.button("Run Cipher"):
            try:
                matrix = np.array(eval(matrix_input))
                run_cipher(hill.encrypt if mode=="Encrypt" else hill.decrypt, text_input, matrix)
            except:
                st.error("Invalid matrix format.")
    card("🏔️ Hill Cipher", "Matrix-based encryption.", inputs)

# Transposition Cipher
elif cipher_choice == "Transposition Cipher":
    def inputs():
        key = st.number_input("Key (Columns):", min_value=2, max_value=10, value=3)
        if st.button("Run Cipher"):
            run_cipher(transposition.encrypt if mode=="Encrypt" else transposition.decrypt, text_input, key)
    card("🔀 Transposition Cipher", "Rearrange columns to encrypt.", inputs)

# DES Cipher
elif cipher_choice == "DES Cipher":
    def inputs():
        key = st.text_input("8-character Key:", placeholder="LOCKCODE")
        if st.button("Run Cipher"):
            if len(key.strip()) == 0:
                st.error("Please enter a valid key.")
            else:
                run_cipher(des.encrypt if mode=="Encrypt" else des.decrypt, text_input, key)
    card("🗝️ DES Cipher", "Block cipher encryption using DES.", inputs)

# RSA Cipher
elif cipher_choice == "RSA Cipher":
    with st.container():
        st.markdown("<div class='card'>### 🏛️ RSA Cipher</div>", unsafe_allow_html=True)
        with st.expander("RSA Key Generation & Encrypt/Decrypt", expanded=True):
            col1, col2, col3 = st.columns(3)
            with col1: p = st.number_input("Prime p:", min_value=2, value=11, step=1)
            with col2: q = st.number_input("Prime q:", min_value=2, value=13, step=1)
            with col3: e = st.number_input("Public Exponent e:", min_value=2, value=7, step=1)

            n = p * q
            phi = (p - 1) * (q - 1)
            st.markdown(f"<div class='terminal'>n = {n} | φ(n) = {phi}</div>", unsafe_allow_html=True)

            if rsa.gcd(e, phi) != 1:
                st.error("❌ e must be coprime with φ(n).")
                st.stop()

            d = rsa.mod_inverse(e, phi)
            st.markdown(f"<div class='terminal'>Public Key: (e={e}, n={n}) | Private Key: (d={d}, n={n})</div>", unsafe_allow_html=True)

            if mode == "Encrypt":
                message_num = st.number_input("Number to Encrypt:", min_value=1, max_value=n-1, value=9)
                if st.button("Encrypt"):
                    cipher = rsa.encrypt_number(message_num, e, n)
                    st.markdown(f"<div class='terminal'>🔒 Encrypted Message: {cipher}</div>", unsafe_allow_html=True)
            else:
                cipher_num = st.number_input("Cipher Number to Decrypt:", min_value=1, max_value=n-1, value=1)
                if st.button("Decrypt"):
                    plain = rsa.decrypt_number(cipher_num, d, n)
                    st.markdown(f"<div class='terminal'>🔓 Decrypted Message: {plain}</div>", unsafe_allow_html=True)
