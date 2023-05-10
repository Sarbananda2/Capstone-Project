from Crypto.Cipher import AES
import base64
import hashlib


"""
Function Description
01. No. of Parameters: Zero
02. Purpose: 
    > Accepts Input from the User
    > Generates Hash of the Input
    > Returns 128-bit / 16-byte Byte Object as Key
03. Output Data Type: Byte Object
"""
def takeKey(key):
  # Accept Key from the User
  userInput = key

  # Generate hash using SHA-512 algorithm
  hash_obj = hashlib.sha512(userInput.encode())

  # Generating Hash Digest String and converting it to Byte Object
  hashAsByteObject = (hash_obj.hexdigest()).encode()
  
  return hashAsByteObject[:16]


"""
Function Description
01. No. of Parameters: Two
02. Parameter Descriptions
    > message
      a. Data Type: String
      b. Purpose: Stores the values that would be encrypted by the Function
    > key
      a. Data Type: Byte Object
      b. Purpose: Stores the Key value that would be used to encrypt the plaintext
03. Purpose: Encrypts Message using the Key and returns the Ciphertext
04. Output Data Type: String
"""
def startAESEncryption(message, key):
  # Set the encryption key (must be 16, 24, or 32 bytes long)
  # key = b'0123456789abcdef'

  # Set the initialization vector (must be 16 bytes long)
  iv = b'0123456789abcdef'

  # Create a new AES cipher object with the key and IV
  cipher = AES.new(key, AES.MODE_CBC, iv)

  # Pad the message to be a multiple of 16 bytes
  padded_message = message + (AES.block_size - len(message) % AES.block_size) * chr(AES.block_size - len(message) % AES.block_size)

  # Encrypt the padded message using the AES cipher
  encrypted_message = cipher.encrypt(padded_message.encode())
  
  # Convert the encrypted message to base64 for easy transport
  encrypted_message_base64 = base64.b64encode(encrypted_message)
  
  # Return the encrypted message in base64 format
  return encrypted_message_base64.decode()


"""
Function Description
01. No. of Parameters: Two
02. Parameter Descriptions
    > encrypted_message_base64
      a. Data Type: String
      b. Purpose: Stores the String value that would be decrypted by the Function
    > key
      a. Data Type: Byte Object
      b. Purpose: Stores the Byte Object value of the Key
03. Purpose: Decrypts message using the Key and returns a Plaintext
04. Output Data Type: String
"""
def startAESDecryption(encrypted_message_base64, key):
  # Set the decryption key (must be 16, 24, or 32 bytes long)
  # key = b'0123456789abcdef'
  
  # Set the initialization vector (must be 16 bytes long)
  iv = b'0123456789abcdef'
  
  # Create a new AES cipher object with the key and IV
  cipher = AES.new(key, AES.MODE_CBC, iv)
  
  # Get the encrypted message from the user
  # encrypted_message_base64 = input("Enter the encrypted message in base64 format: ")
  
  # Convert the encrypted message from base64 to bytes
  encrypted_message = base64.b64decode(encrypted_message_base64)
  
  # Decrypt the encrypted message using the AES cipher
  decrypted_message_padded = cipher.decrypt(encrypted_message)
  
  # Remove the PKCS#7 padding from the decrypted message
  decrypted_message = decrypted_message_padded[:-decrypted_message_padded[-1]].decode()
  
  # Print the decrypted message
  # print("Decrypted message:", decrypted_message)
  return decrypted_message