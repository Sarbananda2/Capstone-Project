# Importing Requirements
import streamlit as st
import Decryptor as dec
import streamlit_lottie
import requests

# Setting Page Configuration
st.set_page_config(
    layout = "wide",
    initial_sidebar_state = "collapsed"
)

# Function Definitions
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Preparing Image
lottie_hello = load_lottieurl(
    "https://assets5.lottiefiles.com/packages/lf20_i1e4j8gy.json"
)

# Preparaing Session State
if "Plaintext" not in st.session_state:
    st.session_state["Plaintext"]  = ""

if "Ciphertext" not in st.session_state:
    st.session_state["Ciphertext"] = ""

# Set up the two columns
col1, col2 = st.columns(2)

# Add content to the right column
with col2:
    streamlit_lottie.st_lottie(
        lottie_hello,
        key = " "
    )

# Add content to the left column
with col1:
    # Page Title
    st.title("Decryption")

    # Accepting Ciphertext from the User
    ciphertext = st.text_input(
        label = "Ciphered Message",
        placeholder = "Enter a String",
        value = st.session_state["Ciphertext"]
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
        if plaintext is None:
            pass
        else:
            st.info(f'Plaintext: {plaintext}')
            st.session_state["Plaintext"] = plaintext