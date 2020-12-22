import os
import base64

from pbkdf2 import crypt
from fernet import Fernet

r = "\033[00m"
g = "\033[92m"


class DeriveKey():
  """Uses PBKDF2's crypt() function
     to derive a 32-bit key from the password,
     using a salt and 100000 iterations

     self.password: User input. There are no restrictions
                    on password complexity.

     self.salt: A previously randomly generated string,
                must be *at least* 16 bytes long;
                according to http://www.ietf.org/rfc/rfc2898.txt

     self.key: Whatever is returned by crypt(), we use this
                in EncryptFiles() / DecryptFiles()

  """
  def __init__(self):
    self.key = None


  def get_password(self):
    self.password = input("Password: ")


  def derive_key_from_password(self):
    self.salt = "lCqsDNHWCWIVZWrMZNSJnJUvltiYPell"
    self.key = crypt(self.password, self.salt, 100000)


class EncryptFiles():
  """Encrypt all files in a list (obtained with os.listdir())
     using Fernet. Fernet uses AES-128 in CBC MoO.

     self.cipher: The cipher [Fernet()] which we use to
                  encrypt data

     self.selection: List containing all unencrypted files in
                     the directory.

     output_file: The file to which the encrypted data is written;
                  this is formed by taking (filename) + ".xCrypt"
  """

  def __init__(self):
    self.cipher = None


  def look_for_files(self, directory):
    self.selection = []
    for filename in os.listdir(directory):
      if os.path.isfile(filename):
        if not filename[len(filename)-6:len(filename)] == ".xCrypt":
        # filter out already encrypted files
          self.selection.append(filename)


  def set_fernet_cipher(self, key):
    key = key[0:32]
    key = bytes(key.encode("utf-8"))
    self.cipher = Fernet(base64.b64encode(key))
    # Fernet requires base64-encoded keys


  def encrypt_selection(self):
    chunk_size = 64*1024

    for input_file in self.selection:
      output_file = input_file + ".xCrypt"

      with open(input_file, "rb") as infile:
        with open(output_file, "wb") as outfile:

          while True:
            chunk = infile.read(chunk_size)
            if len(chunk) == 0:
              break

            outfile.write(self.cipher.encrypt(chunk))

    return True


class DecryptFiles():
  """Decrypt all files in a list (obtained with os.listdir())
     using Fernet.
     Fernet uses AES-128 in CBC MoO.

     self.cipher: The cipher [Fernet()] which we use to
                  decrypt data

     self.selection: List containing all encrypted files in
                     the directory.

     output_file: The file to which the decrypted data is written;
                  this is formed by taking (filename) - ".xCrypt"
  """
  def __init__(self):
    self.cipher = None


  def look_for_files(self, directory):
    self.selection = []
    for filename in os.listdir(directory):
      if os.path.isfile(filename):
        if filename[len(filename)-7:len(filename)] == ".xCrypt":
          self.selection.append(filename)


  def set_fernet_cipher(self, key):
    key = key[0:32]
    key = bytes(key.encode("utf-8"))
    self.cipher = Fernet(base64.b64encode(key))


  def decrypt_selection(self):
    chunk_size = 64*1024

    for input_file in self.selection:
      output_file = input_file[0:len(input_file)-7] # Strip ".xCrypt"

      with open(input_file, "rb") as infile:
        with open(output_file, "wb") as outfile:

          while True:
            chunk = infile.read(chunk_size)
            if len(chunk) == 0:
              break

            outfile.write(self.cipher.decrypt(chunk))

    return True


def main():
  print("reset")
  print("{}[1]{} Encrypt files".format(g, r))
  print("{}[2]{} Decrypt files".format(g, r))

  while True:
    menu = input("Make a choice: ")
    if menu in ["1", "2"]:
      break

  if menu == "1":
    print("\n")
    derive = DeriveKey()
    derive.get_password()

    print("Deriving key...")
    derive.derive_key_from_password()
    print("{}Key derived.{}".format(g, r))

    key = derive.key

    while True:
      dir_ = input("Directory: ")
      if os.path.isdir(dir_):
        break

    encrypt = EncryptFiles()
    encrypt.seek_files(dir_)
    encrypt.set_cipher(key)

    print("Encrypting files...")
    encrypt.encrypt_selection()
    print("{}Files encrypted.{}".format(g, r))

  else:
    print("\n")
    derive = DeriveKey()
    derive.get_password()

    print("Deriving key...")
    derive.derive_key_from_password()
    print("{}Key derived.{}".format(g, r))

    key = derive.key

    while True:
      dir_ = input("Directory: ")
      if os.path.isdir(dir_):
        break

    decrypt = DecryptFiles()
    decrypt.seek_files(dir_)
    decrypt.set_cipher(key)

    print("Decrypting files...")
    decrypt.decrypt_selection()
    print("{}Files decrypted.{}".format(g, r))


if __name__=="__main__":
    main()