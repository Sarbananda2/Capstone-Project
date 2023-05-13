# Importing Requirements
import streamlit as st

import hashlib

def returnHash(text, requiredLength = 0):
    def returnLongHash(hex_dig, requiredLength):
        hexLength = len(hex_dig)
        numerator = requiredLength // hexLength
        denominator = requiredLength % hexLength
        newHash = (hex_dig * numerator) + hex_dig[:denominator]
        return newHash
    
    hash_object = hashlib.sha512(text.encode())
    hex_dig = hash_object.hexdigest()
    print("\nString Hash:", hex_dig)
    
    if len(hex_dig) > requiredLength:
        return hex_dig[:requiredLength]
    elif len(hex_dig) < requiredLength:
        return returnLongHash(hex_dig, requiredLength)
    else:
        return hex_dig
    

user_input = st.text_input("Enter String")
length = st.number_input(
    label = "Enter String Lenght",
)
length = int(length)

returnedHash = returnHash(user_input, length)

#print("String Hash:", returnedHash)
#print("ASCII of Hash:", end = " ")
#for element in returnedHash:
#    print(ord(element), end = " ")
#else:
#    print()
#print("String:", user_input)
#print("Required Length:", length)

st.info(f"String Hash: {returnedHash}")
asciiString = ""
for element in returnedHash:
    asciiString += (str(ord(element)) + " ")
st.info(f"ASCII of Hash: {asciiString}")
st.info(f"String: {user_input}")
st.info(f"Required Length: {length}")