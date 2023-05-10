# importing requirements
import HelperFunctions as hf
import VernamCipher as vc
import FeistelCipher as fc
import AESCipher as ac


def startEncryption(plaintext, VernamKey, FeistelKey, AESKey): 
  """
  Veriable Description
  01. Variable Name: plaintext
  02. Purpose: Store ASCII Values of Initial Plaintext for Encryption
  03. Data Type: List
  
  01. Variable Name: plaintextLength
  02. Purpose: Store Length of Initial Plaintext
  03. Data Type: Integer
  """
  plaintext, plaintextLength = hf.takePlaintext(plaintext)
  
  
  """
  Variable Description
  01. Variable Name: VernamKey
  02. Purpose: Store Key Value for Vernam Cipher
  03. Data Type: List
  
  04. Variable Name: cipherAfterVernamEncryption
  05. Purpose: Store Cipher Value after performing Vernam Cipher
  06. Data Type: List
  """
  VernamKey = vc.takeKey(plaintextLength, VernamKey)
  cipherAfterVernamEncryption = vc.startVernamMagic(plaintext, VernamKey)
  # hf.showOutput(cipherAfterVernamEncryption)
  
  """
  Variable Description
  01. Variable Name: FeistelKey
  02. Purpose: Store Key Value for Feistel Cipher
  03. Data Type: List
  
  04. Variable Name: cipherAfterFeistelEncryption
  05. Purpose: Store Cipher Value after performing Feistel Cipher Encryption
  06. Data Type: List
  """
  FeistelKey = fc.takeKey(plaintextLength, FeistelKey)
  cipherAfterFeistelEncryption = fc.startFeistelEncryption(cipherAfterVernamEncryption, FeistelKey)
  # hf.showOutput(cipherAfterFeistelEncryption)


  """
  Variable Description
  01. Variable Name: cipherInString
  02. Purpose: Stores the String Value for converting the ASCII List of Ciphertext to String
  03. Data Type: String

  04. Variable Name: AESKey
  05. Purpose: Store Key Value for AES Cipher
  06. Data Type: Byte Object

  07. Variable Name: cipherAfterAESEncryption
  08. Purpose: Store Cipher Value after performing AES Cipher Encryption
  09. Data Type: String
  """
  cipherInString = hf.returnStringOfASCII(cipherAfterFeistelEncryption)
  AESKey = ac.takeKey(AESKey)
  cipherAfterAESEncryption = ac.startAESEncryption(cipherInString, AESKey)


  return cipherAfterAESEncryption
  # Printing the Ciphertext to the Screen
  # hf.showCiphertext(cipherAfterAESEncryption, )