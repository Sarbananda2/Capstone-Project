import streamlit as st
import Decryptor as dec

# Page Title
st.title("Decryption")

# Accepting Ciphertext from the User
ciphertext = st.text_input(
    label = "Ciphered Message",
    placeholder = "Enter a String"
)

# Waiting till Ciphertext is entered by the User
if not ciphertext:
    st.stop()

# Accepting Key for Vernam Cipher from the User
keyForVernamCipher = st.text_input(
    label = "Key for Vernam Cipher",
    type = "password",
    placeholder = "Enter a String greater than 10 characters"
)

# Waiting till Key is entered by the User
if not keyForVernamCipher:
    st.stop()

# Accepting Key for Feistel Cipher from the User
keyforFeistelCipher = st.text_input(
    label = "Key for Feistel Cipher",
    type = "password",
    placeholder = "Enter a String"
)

# Waiting till Message is entered by the User
if not keyforFeistelCipher:
    st.stop()

# Accepting Key for AES Cipher from the User
keyForAES = st.text_input(
    label = "Key for AES Cipher",
    type = "password",
    placeholder = "Enter a String"
)

# Waiting till Message is entered by the User
if not keyForAES:
    st.stop()

# Triggering Encryption
button = st.button(
    label = "Decrypt"
)

# Displaying Output
if button:
    plaintext = dec.startDecryption(ciphertext, keyForAES, keyforFeistelCipher, keyForVernamCipher)
    st.info(f'Plaintext: {plaintext}')