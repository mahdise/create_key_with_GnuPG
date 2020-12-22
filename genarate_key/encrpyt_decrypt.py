#https://levelup.gitconnected.com/encrypt-and-decrypt-files-using-python-python-programming-pyshark-a67774bbf9f4
# encryption of files
from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open('mykey.key', 'wb') as mykey:
    mykey.write(key)

with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

print('MyKEy',key)


f = Fernet(key)
file_name = 'raw_file.txt'

def file_encryption():
    with open(file_name, 'rb') as original_file:
        original = original_file.read()
    encrypted = f.encrypt(original)


    """ To check the encrypted file"""

    with open ('encrypted_' + file_name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    return encrypted

print(file_encryption())


    #Decryption files

f = Fernet(key)
file_name = 'raw_file.txt'
with open('encrypted_' + file_name, 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('decrypted_' + file_name, 'wb') as decrypted_file:
    decrypted_file.write(decrypted)

