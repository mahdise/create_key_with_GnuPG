import gnupg


def create_key():

    gpg = gnupg.GPG(gpgbinary=r'C:\Users\Mahdi Islam\Documents\github_\create_key_with_GnuPG\GnuPG\bin\gpg.exe')
    input_data = gpg.gen_key_input(
        passphrase='passphrase',
        name_email='testgpguser@mydomai.com',
    )

    key_from_gnupg = gpg.gen_key(input_data)

    key_convert_to_string = str(key_from_gnupg)

    print("Generated key :", key_convert_to_string)

    return key_convert_to_string, gpg


def encrypt_file(gpg_object,  new_key, file_path = None):

    gpg_ = gnupg.GPG(gpgbinary=r'C:\Users\Mahdi Islam\Documents\github_\create_key_with_GnuPG\GnuPG\bin\gpg.exe')

    with open('my-unencrypted.txt', 'rb') as f:
        status = gpg_.encrypt_file(
            f, recipients=[new_key],passphrase = "passphrase",
            output='my-encrypted.txt.gpg')
    print('ok: ', status.ok)
    print('status: ', status.status)
    print('stderr: ', status.stderr)
    if status.ok:
        result_of_encrypt = "passed"
    else:
        result_of_encrypt = "failed"

    return result_of_encrypt


def split_share(key):
    pass

    return "share part"


def recombine_key(share_of_two):
    pass

    return "key"


def decrypt_file(file_path, old_key):
    gpg_dec = gnupg.GPG(gpgbinary=r'C:\Users\Mahdi Islam\Documents\github_\create_key_with_GnuPG\GnuPG\bin\gpg.exe')

    with open('my-encrypted.txt.gpg', 'rb') as f:
        status = gpg_dec.decrypt_file(f, passphrase='parasea', output='my-decrypted.txt')
    print('stderr: ', status.stderr)
    if status.ok:
        result_of_decrypt = "passed"
    else:
        result_of_decrypt = "failed"

    return result_of_decrypt


if __name__ == '__main__':
    # to encrypt the file
    file_path_for_encrypt = None
    new_key, gpg_main_object = create_key()
    # new_key = "C1C5710259D65A457312AD580F42881B5ABBED92"
    # print(new_key)

    #
    # file_encrypt = encrypt_file(gpg_main_object,new_key)
    print("Encryted file : ",None)
    # print("Result for encrypt file", file_encrypt)
    #
    # split_key = split_share(new_key)
    #
    # # to decrypt the file
    # share_two_part = None
    # recombine_old_key = recombine_key(share_two_part)
    # file_path_for_decrypt = None
    file_decrypt = decrypt_file(None, new_key)
    # print("Result for decrypt file", file_decrypt)
