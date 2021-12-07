from cryptography.fernet import Fernet
import ctypes
from tkinter.filedialog import askopenfilename

def generateKey():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as fileKey:
        fileKey.write(key)
    
    # Inform the user
    ctypes.windll.user32.MessageBoxW(0, "Key has been successfully generated", "SUCCES", 0)
    

def encrypt():
    # Open key and put the key in a var
    with open('key.key', 'rb') as fileKey:
        key = fileKey.read()
    fernet = Fernet(key)

    # Open the file to encrypt
    fileToEncrypt = askopenfilename()
    with open(fileToEncrypt, 'rb') as file:
        fileEncrypt = file.read()

    # Encrypt the file
    encrypted = fernet.encrypt(fileEncrypt)

    with open(fileToEncrypt, 'wb') as encryptedFile:
        encryptedFile.write(encrypted)

    # Inform the user
    ctypes.windll.user32.MessageBoxW(0, "The file has been correctly encrypted", "SUCCES", 0)



def decrypt():
    # Open key and put the key in a var
    with open('key.key', 'rb') as fileKey:
        key = fileKey.read()
    fernet = Fernet(key)    
    # Open the encrypted file
    fileToDecrypt = askopenfilename()
    with open(fileToDecrypt, 'rb') as encryptedFile:
        encrypted = encryptedFile.read()
    
    # Decrypt the file
    decrypted = fernet.decrypt(encrypted)

    with open(fileToDecrypt, 'wb') as file:
        file.write(decrypted)

    # Inform the user
    ctypes.windll.user32.MessageBoxW(0, "The file has been correctly decrypted", "SUCCES", 0)