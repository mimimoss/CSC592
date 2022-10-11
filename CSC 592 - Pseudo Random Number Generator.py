import random
import time

randomSeed = int(time.time())

random.seed(randomSeed)

message = input("Please enter a message: ")

lengthMessage = len(message)

key = random.randbytes(lengthMessage)

encodedMessage = message.encode()
byteArray = bytearray(encodedMessage)

#print(byteArray)

encodedString = bytes([_a ^ _b for _a, _b in zip(byteArray, key)])

decryptedString = bytes([_a ^ _b for _a, _b in zip(encodedString, key)])

decrypted = decryptedString.decode()

print("Random String:", randomSeed)
print("Decrypted Message:", decrypted)
print("Pseudo random string:", key)
print("Output Byte:", encodedString)

