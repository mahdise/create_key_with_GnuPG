import gnupg
import cryptography


def create_key():

    gpg = gnupg.GPG()
    input_data = gpg.gen_key_input(
        passphrase='passphrase',
    )

    key_from_gnupg = gpg.gen_key(input_data)

    key_convert_to_string = str(key_from_gnupg)

    return key_convert_to_string


# def encrypt_file( new_key, file_path = None):
#     print('New Keyyyyyyyyyy',new_key)
#
#     gpg = gnupg.GPG()
#
#     unencrypted_string = 'Who are you? How did you get in my house?'
#     encrypted_data = gpg.encrypt(unencrypted_string, 'testgpguser@mydomain.com')
#     encrypted_string = str(encrypted_data)
#
#     print('ok: ', encrypted_data.ok)
#     print('status: ', encrypted_data.status)
#     print('stderr: ', encrypted_data.stderr)
#     print('unencrypted_string: ', unencrypted_string)
#     print('encrypted_string: ', encrypted_string)
#
#     return "unsuccessful"

new_key = create_key()

f = new_key
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
    #new_key = create_key()
    # new_key = "C1C5710259D65A457312AD580F42881B5ABBED92"
    # print(new_key)

    #
    #file_encrypt = encrypt_file(new_key)
    #print("Result for encrypt file", file_encrypt)

    split_key = split_share(new_key)

    # to decrypt the file
    share_two_part = None
    recombine_old_key = recombine_key(share_two_part)
    file_path_for_decrypt = None
    file_decrypt = decrypt_file(file_path_for_decrypt, recombine_old_key)
    print("Result for decrypt file", file_decrypt)
    print(new_key)