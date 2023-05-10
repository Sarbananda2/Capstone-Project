# Importing Requirements
import hashlib
import VernamCipher as vc


"""
Function Description
01. No. of Parameters: Two
02. Parameter Descriptions
    > hex_dig
      a. Data Type: String
      b. Purpose: String that needs to be extended upto a Length Value
    > requiredLength
      a. Data Type: Integer
      b. Purpose: Value that much the equal to the new String
03. Purpose: Function would return a new String by iterating over from the beginning of the String, so it matchhes the same length as required
04. Output Data Type: String
"""
def returnLongHash(hex_dig, requiredLength):
  hexLength = len(hex_dig)
  numerator = requiredLength // hexLength
  denominator = requiredLength % hexLength
  newHash = (hex_dig * numerator) + hex_dig[:denominator]
  return newHash


"""
Function Description
01. No. of Parameters: Two
02. Parameter Descriptions
    > text
      a. Data Type: String
      b. Purpose: Random String of whose Hash Digest would be generated
    > requiredLength
      a. Data Type: Integer
      b. Purpose: Length of Hash Digest that would be returned
03. Purpose: Function would create a List of Hash Digest as per number of rounds and returned it
04. Output Data Type: String
"""
def returnHash(text, requiredLength = 0):
  hash_object = hashlib.sha512(text.encode())
  hex_dig = hash_object.hexdigest()

  if len(hex_dig) > requiredLength:
      return hex_dig[:requiredLength]
  elif len(hex_dig) < requiredLength:
      return returnLongHash(hex_dig, requiredLength)
  else:
      return hex_dig


"""
Function Description
01. No. of Parameters: Three
02. Parameter Descriptions
    > rawKey
      a. Data Type: String
      b. Purpose: Starting String from which Key List would be derived
    > requiredKeyLength
      a. Data Type: Integer
      b. Purpose: Length of the individual keys inside the Key List
    > numberOfKeys
      a. Data Type: Integer
      b. Purpose: Length of the Key List
03. Purpose: Function would create a List of Hash Digest as per number of rounds and returned it
04. Output Data Type: List
"""
def returnKeyList(rawKey, requiredKeyLength, numberOfKeys = 16):
  """
  Variable Description
  01. Name: currentRawKey
  02. Purpose: Store the String would be used as Raw Key for each Iterations
  03. Data Type: String
  """
  currentRawKey = rawKey

  """
  Variable Description
  01. Name: currentHash
  02. Purpose: Store the Hash of Raw Key for each Iterations
  03. Data Type: String

  04. Name: currentHashList
  05. Purpose: Store the List of ASCII values of the Hash String for each Iteration
  """
  currentHash, currentHashList = "", []

  """
  Variable Description
  01. Name: keyList
  02. Purpose: Store the List of the List of ASCII values of the Hash of the Raw Key
  03. Data Type: List
  """
  keyList = []

  for i in range(numberOfKeys):
    currentHash = returnHash(currentRawKey, requiredKeyLength)
    currentHashList = [ord(x) for x in currentHash]
    keyList.append(currentHashList)
    currentRawKey = currentHash
    
  return keyList


## Encryption Functions
"""
Function Description
01. No. of Parameters: One
02. Parameter Descriptions
    > plaintext
      a. Data Type: List
      b. Purpose: List for figuring out the individual Key Length
03. Purpose: Function would accept a Key from the user and from this Key, it would generate a new List of Keys that would used for each rounds in the Encryption
04. Output Data Type: List
"""
def takeKey(plaintextLength, key):
  # Finds and stores length of the required key
  if plaintextLength % 2 == 0:
    requiredKeyLength = plaintextLength // 2
  else:
    requiredKeyLength = (plaintextLength + 1) // 2
    
  # Stores raw key accepted from the User | Data Type: String
  rawKey = key
  
  # Stores the Hash Digest of the raw key | Data Type: List
  keyList = returnKeyList(rawKey, requiredKeyLength)

  return keyList


"""
Function Description
01. No. of Parameters: Three
02. Parameter Descriptions
    > leftHandSide
    a. Data Type: List
    b. Purpose: Left Hand Side of the plaintext after split
    > rightHandSide
    a. Data Type: List
    b. Purpose: Right Hand Side of the plaintext after split
    > keyValue
    a. Data Type: List
    b. Purpose: Key for the Round
03. Purpose: Function would accept two halves of plaintext, key, performs sub-encryptions, and returns new two halves of ciphertext for next round
04. Output Data Type: List, List
"""
def generateOutputForNextRoundForEncryption(leftHandSide, rightHandSide, key):
  # performing sub-encryptions
  resultAfterFunctionF = vc.startVernamMagic(rightHandSide, key)
  resultAfterPerformingXOR = vc.startVernamMagic(resultAfterFunctionF, leftHandSide)
  
  # ruturning output for next round
  return rightHandSide, resultAfterPerformingXOR


"""
Function Description
01. No. of Parameters: Three
02. Parameter Descriptions
    > plaintext
      a. Data Type: List
      b. Purpose: Stores the plaintext that would be encrypted by the function
    > key
      a. Data Type: List
      b. Purpose: Stores the key that would be used to encrypt the plaintext by the function
    > numberOfRounds
      a. Data Type: Integer
      b. Purpose: Stores the value of how many rounds the Encryption Function must do
03. Parameters Data Type: List, List
04. Function Purpose: This function encrypts plaintext using the key, and generates a ciphertext
05. Output Data Type: List
"""
def startFeistelEncryption(plaintext, key, numberOfRounds = 16):
  # Storing plaintext length for further use
  plaintextLength = len(plaintext)
  
  # adding a space into the plaintext, incase it's length is odd
  if (plaintextLength % 2 != 0):
      plaintext.append(32)
      plaintextLength += 1

  # Splitting plaintext
  leftHandSide = plaintext[:int(plaintextLength / 2)]
  rightHandSide = plaintext[int(plaintextLength / 2):]

  # Performing Encryption
  for i in range(numberOfRounds):
    leftHandSide, rightHandSide = generateOutputForNextRoundForEncryption(leftHandSide, rightHandSide, key[i])

  # Returning values
  return rightHandSide + leftHandSide
  

## Decryption Functions
"""
Function Description
01. No. of Parameters: Three
02. Parameter Descriptions
    > leftHandSide
      a. Data Type: List
      b. Purpose: Left Hand Side of the ciphertext after split
    > rightHandSide
      a. Data Type: List
      b. Purpose: Right Hand Side of the ciphertext after split
    > keyValue
      a. Data Type: List
      b. Purpose: Key for the Round
03. Purpose: Function would accept two halves of plaintext, key, performs sub-encryptions, and returns new two halves of ciphertext for next round
04. Output Data Type: List, List
"""
def generateOutputForNextRoundForDecryption(leftHandSide, rightHandSide, key):
  # performing sub-encryptions
  resultAfterPerformingXOR0 = vc.startVernamMagic(leftHandSide, key)
  resultAfterPerformingXOR1 = vc.startVernamMagic(resultAfterPerformingXOR0, rightHandSide)
  
  # ruturning output for next round
  return resultAfterPerformingXOR1, leftHandSide


"""
Function Description
01. No. of Parameters: Two
02. Parameter Descriptions
    > ciphertext
      a. Data Type: List
      b. Purpose: Stores the ciphertext that would be encrypted by the function
    > key
      a. Data Type: List
      b. Purpose: Stores the key that would be used to encrypt the plaintext by the function
    > numberOfRounds
      a. Data Type: Integer
      b. Purpose: Stores the value of how many rounds the Decryption Function must do
03. Parameters Data Type: List, List
04. Function Purpose: This function encrypts plaintext using the key, and generates a ciphertext
05. Output Data Type: List, Integer
"""
def startFeistelDecryption(ciphertext, key, numberOfRounds = 16):
  # Storing ciphertext length for further use
  ciphertextLength = len(ciphertext)
  
  # Splitting ciphertext
  leftHandSide = ciphertext[int(ciphertextLength // 2):]
  rightHandSide = ciphertext[:int(ciphertextLength // 2)]
  
  # performing decryption
  for i in range(numberOfRounds):
      leftHandSide, rightHandSide = generateOutputForNextRoundForDecryption(leftHandSide, rightHandSide, key.pop())

  # preparing plaintext
  plaintext = leftHandSide + rightHandSide

  # removing a space from the plaintext, incase a space was padded into it during Encryption
  if plaintext[-1] == 32:
    plaintext.pop()
    
  # returning encryption result/ciphertext
  return plaintext, len(plaintext)