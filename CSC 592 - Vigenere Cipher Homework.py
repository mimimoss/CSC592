## ask the user to input file location
## ask the user to encrypt or decrypt
## ask user for a key
## if encrypt open the file, read it, turn each letter into a number, add the numbers from the key

def encrypt(plaintext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext
    print("Your file has been encrypted: ", ciphertext)
    outputFile = open(file + "_end", "w")
    outputFile.write(ciphertext)
    outputFile.close()

def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext
    print("Your file has been decrypted: ", plaintext)

#main

file = input("Enter file path: ")
plaintext = open(file, "r")
key = input("Enter key: ")
encryptOrDecrypt = input("Enter e for encryption or d for decryption: ")

if encryptOrDecrypt == "d":
    decrypt(ciphertext, key)
elif encryptOrDecrypt == "e":
    encrypt(plaintext, key)
    

