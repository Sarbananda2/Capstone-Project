import streamlit as st

user_input = [int(x) for x in st.text_input("Enter List 01: ").strip().split()]
keyList = [int(x) for x in st.text_input("Enter List 02: ").strip().split()]

try:
    def showOutput():
        # print("Output:", end = " ")
        newString = ""
        for i in range(len(user_input)):
            newString += (str(user_input[i] ^ keyList[i]) + " ")
            # print(user_input[i] ^ keyList[i], end = " ")
        st.info(f"Output: {newString}")

    if st.button("XOR Now!"):
        showOutput()
except:
    st.info("Something is wrong with the list.")