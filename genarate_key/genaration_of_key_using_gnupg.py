import gnupg
import cryptography
from cryptography.fernet import Fernet
from pyseltongue import PlaintextToHexSecretSharer


def create_key():

    gpg = gnupg.GPG()
    input_data = gpg.gen_key_input()

    key_from_gnupg = gpg.gen_key(input_data)

    key_convert_to_string = str(key_from_gnupg)

    return key_convert_to_string


def encrypt_file(new_key, file_path=None):
    print(new_key)

    gpg = gnupg.GPG(gnupghome="new")

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
    thresHold = 2
    shareHolder = 5
    shares = PlaintextToHexSecretSharer.split_secret(
        key, thresHold, shareHolder)
    return shares


def recombine_key(key1, key2):

    return PlaintextToHexSecretSharer.recover_secret([key1, key2])


def decrypt_file(file_path, old_key):
    pass

    return "unsuccessful"


if __name__ == '__main__':
    # to encrypt the file
    file_path_for_encrypt = None
    new_key = create_key()
    new_key = '092F12883619EA9A95F804BDE72C50BF3D2113A35'
    print(new_key)
    shares = split_share(new_key)
    print(shares)
    print(recombine_key(shares[0], shares[1]))
