"""
Building a Caesar Cipher

Challenge: Secret Message Encryptor & Decryptor

Create a Python script that helps you send secret messages to your friend using simple encryption.

Your program should:
1. Ask the user if they want to (E)ncrypt or (D)ecrypt a message.
2. If encrypting:
   - Ask for a message and a numeric secret key.
   - Use a Caesar Cipher (shift letters by the key value).
   - Output the encrypted message.
3. If decrypting:
   - Ask for the encrypted message and key.
   - Reverse the encryption to get the original message.

Rules:
- Only encrypt letters; leave spaces and punctuation as-is.
- Make sure the letters wrap around (e.g., 'z' + 1 → 'a').

Bonus:
- Allow uppercase and lowercase letter handling
- Show a clean interface
"""

import os
import sys

def encrypt(message,key):
    result = ""

    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key) % 26 + base
            result += chr(shifted)
        elif char == " ":
            result += "@"
        else:
            result +=char
    return result


def decrupt(messages,key):
    result = ""
    for char in messages:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base - key) % 26 + base
            result += chr(shifted)
        elif char == "@":
            result += " "
        else:
            result +=char
    return result
            


while True:
    os.system('cls')
    print("Secert Message Program")
    choices = input("Do you want to E or D and X for exit the program ").strip().lower()

    if choices == 'e':
        os.system('cls')
        text = input("Enter your message  \n")
        try:
            key = int(input("Enter a Number between 1 and 25 "))
            # os.system('cls')
            result = encrypt(text,key)
            print("\n Encrypted Message: ")
            print(result) 
        except ValueError:
            print(" invalid key ")
            
    elif choices == 'd':
        text = input("Enter your Encrypted Message\n")
        try:
            key = int(input("Please enter your 1 letter key b/w 1 - 25"))
            # os.system('cls')
            result = decrupt(text,key)
            print("\n Decrypted Message: ")
            print(result)
            
        except ValueError:
            print("--invalid key--")
    elif choices == 'x':
        print("GOOD BYEE...☺")
        break
    
    else:
        print("Invalid Choice")
    
        