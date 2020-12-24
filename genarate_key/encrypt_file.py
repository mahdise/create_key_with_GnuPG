import gnupg
import os
from pyseltongue import PlaintextToHexSecretSharer
from save_split import save_split_file


def create_key():
    """
    This method used for generate jey using gpg
    :return: gpg key which type is string, gpg object
    """
    # create gpg object
    # gpg = gnupg.GPG(gpgbinary='../GnuPG/bin/gpg.exe')
    gpg = gnupg.GPG(gpgbinary='GnuPG/bin/gpg.exe')

    # input necessary input relate to key
    input_data = gpg.gen_key_input(
        passphrase='passphrase',
        name_email='testgpguser@mydomai.com',
    )

    # original key object
    key_from_gpg = gpg.gen_key(input_data)

    # key convert to staring
    key_convert_to_string = str(key_from_gpg)

    # print("Generated key :", key_convert_to_string)

    return key_convert_to_string, gpg


def encrypt_file(gpg_object, new_key, file_path=None):
    """
    This method used for encrypt file using gpg.
    At this moment single file is support for this method but
    in future we could develop for multiple file.

    :param gpg_object: same object created by create key method
    :param new_key: key from gpg
    :param file_path: absolute path for encrypt
    :return: after encrypt return the status of the method either passed or failed
    """
    # create gpg object
    # gpg_ = gnupg.GPG(gpgbinary='../GnuPG/bin/gpg.exe')
    gpg_ = gnupg.GPG(gpgbinary='GnuPG/bin/gpg.exe')

    # read file for encrypt
    with open(file_path, 'rb') as each_file:
        status = gpg_.encrypt_file(
            each_file, recipients=[new_key], passphrase="passphrase", sign=False,
            always_trust=True,
            output=filePath + ".gpg")

    # create status for this method
    if status.ok:
        result_of_encrypt = "passed"
    else:
        result_of_encrypt = "failed"

    return result_of_encrypt


def split_share(key, file_name):
    """
    This method is used for create share from key based
    on shamir secret share algorithm.
    Now at this moment, we gave share holder five and threshold
    two. In a future, we could dynamic based on user wish.

    :param key: key from gpg
    :param file_name: absolute file path
    :return: after split into share return share as list
    """
    # As in library has little bug , we are trying here to remove

    if key[0] == "0":
        string_list = list(key)
        string_list[0] = "-"

        key_convert_to_string = "".join(string_list)

    else:
        key_convert_to_string = key

    # default value for share holder and thresh hold
    thresh_hold = 2
    share_holder = 5

    # call method form split share the key
    shares = PlaintextToHexSecretSharer.split_secret(
        key_convert_to_string, thresh_hold, share_holder)

    # to save the share part into store share code
    result = save_split_file(shares, file_name)

    print("Status Save share part : ", result)

    return shares


if __name__ == '__main__':

    # user input for path
    filePath = input("Enter file path for encrypt: ")
    # try to read path
    if os.path.exists(filePath):
        new_key_from_gpg, gpg_main_object = create_key()
        file_encrypt = encrypt_file(gpg_main_object, new_key_from_gpg, filePath)
        print("Status of file encrypt : ", file_encrypt)
        split_key = split_share(new_key_from_gpg, filePath)

    else:
        print("Path doesn't exist")
