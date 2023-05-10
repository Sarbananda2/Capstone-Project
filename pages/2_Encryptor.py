# Importing Requirements
import streamlit as st
import Encryptor as enc


# Page Title
st.title("Encryption")


# Accepting Message from the User
message = st.text_input(
    label = "Plain Message",
    placeholder = "Enter a String"
)

# Waiting till Message is entered by the User
if not message:
    st.stop()
else:
    messageLength = len(message)


# Accepting Key for Vernam Cipher from the User
keyForVernamCipher = st.text_input(
    label = "Key for Vernam Cipher",
    type = "password",
    placeholder = f"Enter a String smaller than or equal to {messageLength} characters"
)

# Waiting till Key is entered by the User
if not keyForVernamCipher:
    st.stop()
else:
    if len(keyForVernamCipher) > messageLength:
        st.warning(f"Enter a String smaller than or equal to {messageLength} characters")
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
    label = "Encrypt", 
)

# Displaying Output
if button:
    ciphertext = enc.startEncryption(message, keyForVernamCipher, keyforFeistelCipher, keyForAES)
    st.info(f'Ciphertext: {ciphertext}')