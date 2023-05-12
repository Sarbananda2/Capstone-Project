# importing requirements
import HelperFunctions as hf
import VernamCipher as vc
import FeistelCipher as fc
import AESCipher as ac
import streamlit as st


def startDecryption(ciphertext, AESKey, FeistelKey, VernamKey):
  """
  Variable Description
  01. Variable Name: ciphertext
  02. Purpose: Stores the Raw Ciphertext entered by the User
  03. Data Type: String

  04. Variable Name: AESKey
  05. Purpose: Stores the Byte Object after it generated from the Raw Key accepted from the User
  06. Data Type: Byte Object

  07. Variable Name: ciphertextAfterAESDecryption
  08. Purpose: Stores the Decrypted Message generated after Decrypting the Ciphertext
  09. Data Type: String

  10. Variable Name: cipherInASCII
  11. Purpose: Stores the ASCII List of the Decrypted Message String after generating it
  12. Data Type: List

  13. Variable Name: ciphertextLength
  14. Purpose: Stores the Length of the Ciphertext
  13. Data Type: Integer
  """
  ciphertext = hf.takeCiphertextForAES(ciphertext)
  AESKey = ac.takeKey(AESKey)
  ciphertextAfterAESDecryption = ac.startAESDecryption(ciphertext, AESKey)
  cipherInASCII, ciphertextLength = hf.returnASCIIofString(ciphertextAfterAESDecryption)

  # checking if ciphertext or key is valid or not
  if ciphertextLength == 0:
    st.info("Either Ciphertext or keys are invalid")
    return


  """
  Variable Description
  01. Variable Name: FeistelKey
  02. Purpose: Store Key Value for Feistel Cipher
  03. Data Type: List
  
  04. Variable Name: messageAfterFeistelDecryption
  05. Purpose: Store Message Value after performing Feistel Cipher Decryption
  06. Data Type: List
  """
  FeistelKey = fc.takeKey(ciphertextLength, FeistelKey)
  messageAfterFeistelDecryption, ciphertextLength = fc.startFeistelDecryption(cipherInASCII, FeistelKey)
  # hf.showOutput(messageAfterFeistelDecryption)

  
  """
  Variable Description
  01. Variable Name: VernamKey
  02. Purpose: Store Key Value for Vernam Cipher
  03. Data Type: List
  
  04. Variable Name: cipherAfterVernamEncryption
  05. Purpose: Store Cipher Value after performing Vernam Cipher
  06. Data Type: List

  07. Variable Name: ciphertextLength
  08. Purpose: Stores the Length of the Ciphertext
  09. Data Type: Integer
  """
  ciphertextLength = len(messageAfterFeistelDecryption)
  VernamKey = vc.takeKey(ciphertextLength, VernamKey)
  messageAfterVernamDecryption = vc.startVernamMagic(messageAfterFeistelDecryption, VernamKey)
  # hf.showOutput(messageAfterVernamDecryption)


  return hf.returnStringOfASCII(messageAfterVernamDecryption)
  # Printing the Plaintext to the Screen
  # hf.showPlaintext(messageAfterVernamDecryption)