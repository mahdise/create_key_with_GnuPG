import gnupg
import os
from pyseltongue import PlaintextToHexSecretSharer


def recombine_key(key1, key2):
    create_old_key_from_share_part = PlaintextToHexSecretSharer.recover_secret([
        key1, key2])

    if create_old_key_from_share_part[0] == "-":
        string_list = list(create_old_key_from_share_part)
        string_list[0] = "0"

        create_old_key_from_share_part = "".join(string_list)

    return create_old_key_from_share_part


def decrypt_file(file_path, old_key, password="passphrase"):
    gpg_dec = gnupg.GPG(gpgbinary='../GnuPG/bin/gpg.exe')
    gpg_dec.import_keys(old_key)

    # process output file name
    replace_file_path = file_path.replace('.gpg', '')
    split_file = replace_file_path.split(".")
    add_suffix = split_file[0] + "_decrypt"
    final_output = add_suffix + "." + split_file[1]

    with open(file_path, 'rb') as f:
        status = gpg_dec.decrypt_file(
            f, passphrase=password, output=final_output)

    if status.ok:
        result_of_decrypt = "passed"
    else:
        result_of_decrypt = "failed"

    return result_of_decrypt


if __name__ == '__main__':

    file_path_for_decrypt = None

    filePath = input("enter filepath: ")
    if (os.path.exists(filePath)):
        file_path_for_decrypt = filePath


    else:
        print("Path dosen't exist")

    if file_path_for_decrypt:
        key_part = input("Please Enter share part (ex 123,122): ")
        split_share_part = key_part.split(",")
        first_share = split_share_part[0]
        second_share = split_share_part[0]

        recombine_old_key = recombine_key(first_share, second_share)

        file_decrypt = decrypt_file(file_path_for_decrypt, recombine_old_key)

        print(" Status of decrypt file : ", file_decrypt)


