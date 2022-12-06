import os
import sys

#Hashicorp Server must be running from terminal first

def main():
    encryptOrDecrypt = input('Please enter e to encrypt a message, or d to decrypt a message: ')
    if encryptOrDecrypt.lower() == 'e':
        config()
        encrypt()
    elif encryptOrDecrypt.lower() == 'd':
        decrypt()
    else:
        print('Please enter either e or d')
        main()
    
def config():
    # set environment variables to work from terminal
    os.environ['VAULT_ADDR'] = 'http://127.0.0.1:8200'

    # get token
    token = input('Secret token: ')
    os.environ['set VAULT_TOKEN'] = token

    # enable transit engine
    print('Enabling the transit secrets engine at: transit/')
    os.system('vault secrets enable transit')

# encrypt plaintext
def encrypt():
    # create encryption key
    print('creating a key of type aes256-gcm96')
    key = input('\Please, enter the desired encryption key name: ')
    os.system('vault write transit/keys/%s type=aes256-gcm96' % key)

    # get plaintext message from user
    message = input('Please enter your message: ')
    print('Please, save your ciphertext for later use!')
    # encrypt user's input with key
    cipherText = os.system('vault write transit/encrypt/%s plaintext=$(base64 <<< "%s")' % (key,message))
    print(cipherText)


# decrypt a ciphertext
def decrypt():
    cipherText = input('Please, enter your ciphertext: ')
    key = input('Please, enter the desired encryption key name: ')
    os.system('echo \' Original Message: \'')
    plainText = os.system('vault write transit/decrypt/%s ciphertext=%s' % (key, cipherText))

    readableFormat = os.system('base64 --decode <<< "%s"' % plainText)
    print(readableFormat)


if __name__ == "__main__":
    main()
