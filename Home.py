# Importing Requirements
import streamlit as st
import streamlit_lottie
import requests
from streamlit_extras.switch_page_button import switch_page

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

# Set the style for the button
st.write(
    "<style>div.row-widget.stButton > button:first-child {width: 200px; height: 50px;}</style>", 
    unsafe_allow_html=True
)

# Preparing Image
lottie_hello = load_lottieurl(
    "https://assets6.lottiefiles.com/packages/lf20_xqy8h6ej.json"
)

# Preparaing Session State
if "Plaintext" not in st.session_state:
    st.session_state["Plaintext"]  = ""

if "Ciphertext" not in st.session_state:
    st.session_state["Ciphertext"] = ""

# Set up the two columns
col1, col2 = st.columns(2)

# Add content to the left column
with col1:
    for i in range(2):
        st.write(" ")

    # Page Title
    st.title("Hey Explorer!")

    # Header
    st.text("Select Operation")

    if st.button(label = "Encryption"):
        switch_page("Encryptor")

    if st.button(label = "Decryption"):
        switch_page("Decryptor")

# Add content to the right column
with col2:
    streamlit_lottie.st_lottie(
        lottie_hello,
        key = " "
    )