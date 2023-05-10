import streamlit as st

# Function to modify/format key/text
def repairKey(length, text):
    textLength = len(text)
    div = length // textLength
    rem = length % textLength    
    newKey = text * div
    newKey += text[:rem]
    return newKey


"""
Function Description
01. Parameter: Length of Plaintext, Datatype: Integer
02. Action: Accepts Key for Vernam Cipher as per rules, reformats key if necessary
03. Output: Key for Vernam Cipher, Datatype: List
"""
def takeKey(plaintextLength, key):
  # Requesting the Key from the User uptill the Input passes the prerequisites
  userinput = key
  userinputLength = len(userinput)
  
  if plaintextLength > userinputLength:
    userinput = repairKey(plaintextLength, userinput)
  elif userinputLength > plaintextLength:
    print("Size Error! Try again.")
    st.info("Something is wrong!")

  # Converting the Key String to ASCII
  userinput = [ord(x) for x in userinput]

  # Returning the Output
  return userinput


"""
Function Description
01. No. of Parameters: Two
02. Parameters: plaintext, key
03. Parameters Data Type: list, list
04. Function Purpose: This function encrypts plaintext using the key, and generates a ciphertext
05. Output: ciphertext
06. Output Data Type: list
"""
def startVernamMagic(plaintext, key):
  plaintextLength = len(plaintext)
  ciphertext = []

  for i in range(plaintextLength):
    ciphertext.append(plaintext[i] ^ key[i])

  return ciphertext