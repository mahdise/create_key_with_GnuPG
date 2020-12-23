import gnupg
import cryptography
from cryptography.fernet import Fernet
key = Fernet.generate_key()
print("<<<<<<<<<<<<<<<<<<",key)

def create_key():

    gpg = gnupg.GPG(gpgbinary=r'C:\Users\Mahdi Islam\Documents\github_\create_key_with_GnuPG\GnuPG\bin\gpg.exe')
    input_data = gpg.gen_key_input(
        passphrase='passphrase',
        name_email='testgpguser@mydomain.com',
    )

    key_from_gnupg = gpg.gen_key(input_data)

    key_convert_to_string = str(key_from_gnupg)

    unencrypted_string = 'Who are you? How did you get in my house?'
    encrypted_data = gpg.encrypt(unencrypted_string, key_convert_to_string)
    encrypted_string = str(encrypted_data)

    print('ok: ', encrypted_data.ok)
    print('status: ', encrypted_data.status)
    print('stderr: ', encrypted_data.stderr)
    print('unencrypted_string: ', unencrypted_string)
    print('encrypted_string: ', encrypted_string)

    print("ok")

    return key_convert_to_string


def encrypt_file( new_key, file_path = None):
    print(new_key)

    gpg = gnupg.GPG(gpgbinary=r'C:\Users\Mahdi Islam\Documents\github_\create_key_with_GnuPG\GnuPG\bin\gpg.exe', gnupghome ="new" )

    unencrypted_string = 'Who are you? How did you get in my house?'
    encrypted_data = gpg.encrypt(unencrypted_string, 'letz@email.com')
    encrypted_string = str(encrypted_data)

    print('ok: ', encrypted_data.ok)
    print('status: ', encrypted_data.status)
    print('stderr: ', encrypted_data.stderr)
    print('unencrypted_string: ', unencrypted_string)
    print('encrypted_string: ', encrypted_string)

    return "unsuccessful"


def split_share(key):
    pass

    return "share part"


def recombine_key(share_of_two):
    pass

    return "key"


def decrypt_file(file_path, old_key):
    pass

    return "unsuccessful"


if __name__ == '__main__':
    # to encrypt the file
    file_path_for_encrypt = None
    new_key = create_key()
    # new_key = "C1C5710259D65A457312AD580F42881B5ABBED92"
    # print(new_key)

    #
    file_encrypt = encrypt_file(new_key)
    # print("Result for encrypt file", file_encrypt)
    #
    # split_key = split_share(new_key)
    #
    # # to decrypt the file
    # share_two_part = None
    # recombine_old_key = recombine_key(share_two_part)
    # file_path_for_decrypt = None
    # file_decrypt = decrypt_file(file_path_for_decrypt, recombine_old_key)
    # print("Result for decrypt file", file_decrypt)
