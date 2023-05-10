"""
Function Description
01. Function Name: takePlaintext
02. No. of Parameters: Zero
03. Parameter Type: N/A
02. Function Purpose: 
  Accepts String Input from the user
  Converts the String Input into List
  Find and Stores the Input Length
03. Output Data Type: Tuple (List, Integer)
"""
def takePlaintext(userinput):
  plaintext = [ord(x) for x in userinput]
  plaintextLength = len(plaintext)
  return plaintext, plaintextLength


"""
Function Description
01. Function Name: convertToASCII
02. No. of Parameters: One
03. Parameter Name: text
04. Parameter Type: String
05. Function Purpose: Creates a new list of ASCII values of the elements of given String Parameter
06. Output Data Type: List
"""
def convertToASCII(text):
  return [ord(x) for x in text]


"""
Function Description
01. No. of Parameters: One
02. Parameter Descriptions
    > dummyList
      a. Data Type: List
      b. Purpose: Function will print the dummyList onto the Screen
04. Function Purpose: Function will print the parameter list onto the Screen
"""
def showOutput(dummyList):
  print(f"Output List: {dummyList}")


"""
Function Description
01. No. of Parameters: One
02. Parameter Descriptions
    > ciphertext
    a. Data Type: List or String
    b. Purpose: Stores List or String of Ciphertext that the function will use to print the Output
03. Purpose: Print the Output String of Ciphertext in Binary
04. Output Data Type: None
"""
def showCiphertext(ciphertext):
  if isinstance(ciphertext, list):
    cipherInBinary = [bin(x)[2:].zfill(8) for x in ciphertext]
    print("\nFinal Ciphertext: {}".format(" ".join(cipherInBinary)))
  else:
    print("\nFinal Ciphertext: {}".format(ciphertext))


"""
Function Description
01. No. of Parameters: One
02. Parameter Descriptions
    > ciphertext
    a. Data Type: List
    b. Purpose: List of Ciphertext that the function will use to check if the Binary List is valid or not
03. Purpose: Function will check whether the given input parameter is a valid list of 8-bits binary numbers or nto
04. Output Data Type: Boolean
"""
def validateCiphertext(ciphertext):
  # Going through all the Binary Elements
  for element in ciphertext:
    # Check if the input string contains only 0 and 1 characters
    if not all(char in '01' for char in element):
        return False
    # Check if the length of the input string is exactly 8
    if len(element) != 8:
        return False
  # If both conditions are true, then the input string is a valid binary number of 8 bits
  return True
  

"""
Function Description
01. No. of Parameters: Zero
02. Purpose: 
    a. Accept the Binary String of the Ciphertext from the User
    b. Convert the Binary String to Binary List
    c. Convert the Binary List to ASCII List
    d. Finds and Stores the Ciphertext Length
    e. Outputs the Ciphertext List and Ciphertext Length
03. Output Data Type: List, Integer
"""
def takeCiphertext():
  while True:
    # Asking for Ciphertext from the User
    userInput = input("Enter Ciphertext: ").strip().split(" ")

    # Validating Ciphertext
    if validateCiphertext(userInput):
      break
    else:
      print("Ciphertext Invalid. Try Again.")

  # Converting Binary List to ASCII List
  ciphertext =  [int(x, 2) for x in userInput]

  # Finding and Storing Ciphertext Length
  ciphertextLength = len(ciphertext)

  # Returning Output
  return ciphertext, ciphertextLength


"""
Function Description
01. No. of Parameters: One
02. Parameter Descriptions
    > plaintext
      a. Data Type: List
      b. Purpose: Stores the ASCII list for the function to use
03. Purpose: The function prints generates a string from the ASCII List and prints it on the screen. 
04. Output Data Type: None
"""
def showPlaintext(plaintext):
  stringToDisplay = ""

  for element in plaintext:
    stringToDisplay += chr(element)
  else:
    print(f"\nOriginal Message: {stringToDisplay}")


"""
Function Description
01. No. of Parameters: One
02. Parameter Descriptions
    > asciiList
      a. Data Type: List
      b. Purpose: Stores the List on which the operations would be performed by the Function
03. Purpose: Function convert the List of ASCII Values to Character String and returns it 
04. Output Data Type: String
"""
def returnStringOfASCII(asciiList):
  newList = [chr(x) for x in asciiList]
  newString = "".join(newList)
  return newString


"""
Function Description
01. No. of Parameters: Zero
02. Purpose: Accept String input from the User and return it
03. Output Data Type: String
"""
def takeCiphertextForAES(userInput):
  userinput = userInput
  return userinput


"""
Function Description
01. No. of Parameters: One
02. Parameter Descriptions
    > dummyString
      a. Data Type: String
      b. Purpose: Store the String value on which the Function would perform operation on
03. Purpose
    > Create a new list with ASCII values of the Character of the String
    > Finds the Length of the New List
    > Return both the New List and its Length
04. Output Data Type: Tuple (List, Integer)
"""
def returnASCIIofString(dummyString):
  newList = [ord(x) for x in dummyString]
  listLength = len(newList)
  return newList, listLength