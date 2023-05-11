# Importing Requirements
import streamlit as st
from streamlit_lottie import st_lottie
import requests

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

    st.button(
        label = "Encryption"
    )

    st.button(
        label = "Decryption"
    )

# Add content to the right column
with col2:
    st_lottie(
        lottie_hello,
        key = " "
    )