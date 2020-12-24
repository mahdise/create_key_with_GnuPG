import gnupg
import os
from pyseltongue import PlaintextToHexSecretSharer
from save_split import save_split_file


def create_key():
    gpg = gnupg.GPG(gpgbinary='../GnuPG/bin/gpg.exe')
    input_data = gpg.gen_key_input(
        passphrase='passphrase',
        name_email='testgpguser@mydomai.com',
    )

    key_from_gnupg = gpg.gen_key(input_data)

    key_convert_to_string = str(key_from_gnupg)

    print("Generated key :", key_convert_to_string)

    return key_convert_to_string, gpg


def encrypt_file(gpg_object, new_key, file_path=None):
    gpg_ = gnupg.GPG(gpgbinary='../GnuPG/bin/gpg.exe')

    with open(file_path, 'rb') as each_file:
        status = gpg_.encrypt_file(
            each_file, recipients=[new_key], passphrase="passphrase", sign=False,
            always_trust=True,
            output=filePath + ".gpg")

    if status.ok:
        result_of_encrypt = "passed"
    else:
        result_of_encrypt = "failed"

    return result_of_encrypt


def split_share(key, file_name=None):
    if key[0] == "0":
        string_list = list(key)
        string_list[0] = "-"

        key_convert_to_string = "".join(string_list)

    thresHold = 2
    shareHolder = 5
    shares = PlaintextToHexSecretSharer.split_secret(
        key, thresHold, shareHolder)

    result = save_split_file(shares, file_name)

    print("Status Save share part : ", result)

    return shares


if __name__ == '__main__':

    filePath = input("Enter file path for encrypt: ")
    if os.path.exists(filePath):
        new_key, gpg_main_object = create_key()
        file_encrypt = encrypt_file(gpg_main_object, new_key, filePath)
        print("Status of file encrypt : ", file_encrypt)

        split_key = split_share(new_key, filePath)

    else:
        print("Path doesn't exist")
