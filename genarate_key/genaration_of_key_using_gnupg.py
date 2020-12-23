import gnupg

from pyseltongue import PlaintextToHexSecretSharer


def create_key():

    # Todo
    # dynamic gpg binary path
    #password

    gpg = gnupg.GPG(gpgbinary='../GnuPG/bin/gpg.exe')
    input_data = gpg.gen_key_input(
        passphrase='passphrase',
        name_email='testgpguser@mydomai.com',
    )

    key_from_gnupg = gpg.gen_key(input_data)

    key_convert_to_string = str(key_from_gnupg)

    print("Generated key :", key_convert_to_string)

    return key_convert_to_string, gpg


def encrypt_file(gpg_object,  new_key, file_path = None):

    gpg_ = gnupg.GPG(gpgbinary='../GnuPG/bin/gpg.exe')

    # Todo
    # dynamic file path with name
    # dynamic pass phrase
    # encrypt multiple file

    with open(r'C:\Users\Mahdi Islam\Documents\salim\ffffffff.txt', 'rb') as each_file:
        status = gpg_.encrypt_file(
            each_file, recipients=[new_key], passphrase="passphrase", sign=False,
            always_trust=True,
            output=r'C:\Users\Mahdi Islam\Documents\salim\ffffffff.txt.gpg')

    if status.ok:
        result_of_encrypt = "passed"
    else:
        result_of_encrypt = "failed"

    return result_of_encrypt


def split_share(key):



    if key[0] == "0":
        string_list = list(key)
        string_list[0] = "-"

        key_convert_to_string = "".join(string_list)



    thresHold = 2
    shareHolder = 5
    shares = PlaintextToHexSecretSharer.split_secret(
        key, thresHold, shareHolder)


    return shares


def recombine_key(key1, key2):


    create_old_key_from_share_part = PlaintextToHexSecretSharer.recover_secret([key1, key2])

    if create_old_key_from_share_part[0] == "-":
        string_list = list(create_old_key_from_share_part)
        string_list[0] = "0"

        create_old_key_from_share_part = "".join(string_list)

    return create_old_key_from_share_part


def decrypt_file(file_path, old_key, password = "passphrase"):
    # Todo
    # dynamic file path with name
    # encrypt multiple file

    gpg_dec = gnupg.GPG(gpgbinary='../GnuPG/bin/gpg.exe')

    with open(r'C:\Users\Mahdi Islam\Documents\salim\ffffffff.txt.gpg', 'rb') as f:
        status = gpg_dec.decrypt_file(f, passphrase=password, output=r'C:\Users\Mahdi Islam\Documents\salim\ffffffff_decryp.txt')

    if status.ok:
        result_of_decrypt = "passed"
    else:
        result_of_decrypt = "failed"

    print("Decrypted file :",result_of_decrypt )

    return result_of_decrypt


if __name__ == '__main__':
    # to encrypt the file
    file_path_for_encrypt = None
    new_key, gpg_main_object = create_key()


    file_encrypt = encrypt_file(gpg_main_object, new_key)

    print("Encryted file : ", file_encrypt)
    # print("Result for encrypt file", file_encrypt)
    #
    split_key = split_share(new_key)
    print("share part", split_key)
    # only for exampale
    frist_share = split_key[1]
    second_share = split_key[4]

    print("First part share :", frist_share)
    print("Second part share :", second_share)
    # # to decrypt the file
    # share_two_part = None
    recombine_old_key = recombine_key(frist_share, second_share)
    print("recover key : ", recombine_old_key)
    # file_path_for_decrypt = None
    file_decrypt = decrypt_file(None, new_key)
    # print("Result for decrypt file", file_decrypt)
