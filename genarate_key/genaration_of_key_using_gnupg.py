def create_key():
    pass

    return "key"


def encrypt_file(file_path, new_key):
    pass

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
    file_encrypt = encrypt_file(file_path_for_encrypt, new_key)
    print("Result for encrypt file", file_encrypt)

    split_key = split_share(new_key)

    # to decrypt the file
    share_two_part = None
    recombine_old_key = recombine_key(share_two_part)
    file_path_for_decrypt = None
    file_decrypt = decrypt_file(file_path_for_decrypt, recombine_old_key)
    print("Result for decrypt file", file_decrypt)
