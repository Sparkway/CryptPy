from cryptography.fernet import Fernet
from art import *
from colorama import Fore, Back, Style

def main():
    print(Fore.GREEN + text2art("CryptPy", font="3d_diagonal") + Style.RESET_ALL)                      

    userChoice = input("1 - Create a key\n2 - Encrypt a file\n3 - Decrypt a file\n4 - Exit the programm\nEnter a number : ")

    if userChoice == '1':
        generateKey()
    elif userChoice == '2':
        encrypt()
    elif userChoice == '3':
        decrypt()
    elif userChoice == '4':
        print("Bye Bye !")
        SystemExit()
    else:
        print("Bad choice, only 1, 2, 3 or 4")

def backToMain():
    # Asks the user if they want to return to the menu
    backToMain = input("Go back to the menu? (y/n only) : ")
    if backToMain == 'y':
        main()
    else:
        print("Bye Bye !")
        SystemExit()

def generateKey():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as fileKey:
        fileKey.write(key)
    print("Key has been successfully generated")
    
    # Asks the user if they want to return to the menu
    backToMain()

def encrypt():
    # Open key and put the key in a var
    with open('key.key', 'rb') as fileKey:
        key = fileKey.read()
    fernet = Fernet(key)

    # Open the file to encrypt
    fileToEncrypt = input("Which file do you want to encrypt? ")
    with open(fileToEncrypt, 'rb') as file:
        fileEncrypt = file.read()

    # Encrypt the file
    encrypted = fernet.encrypt(fileEncrypt)

    with open(fileToEncrypt, 'wb') as encryptedFile:
        encryptedFile.write(encrypted)

    # Inform the user
    print("The file has been correctly encrypted")

    # Asks the user if they want to return to the menu
    backToMain()


def decrypt():
    # Open key and put the key in a var
    with open('key.key', 'rb') as fileKey:
        key = fileKey.read()
    fernet = Fernet(key)    
    # Open the encrypted file
    fileToDecrypt = input("Which file do you want to decrypt? ")
    with open(fileToDecrypt, 'rb') as encryptedFile:
        encrypted = encryptedFile.read()
    
    # Decrypt the file
    decrypted = fernet.decrypt(encrypted)

    with open(fileToDecrypt, 'wb') as file:
        file.write(decrypted)

    # Inform the user
    print("The file has been correctly decrypted")

    # Asks the user if they want to return to the menu
    backToMain()


if __name__ == "__main__":
    main()