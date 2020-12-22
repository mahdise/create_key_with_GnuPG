import gnupg

gpg = gnupg.GPG(binary=r'C:\Users\Mahdi Islam\Documents\github_\create_key_with_GnuPG\GnuPG\bin\gpg.exe',
                ignore_homedir_permissions=True,
                homedir=r'C:\Users\Mahdi Islam\Documents\github_\ffff')
print(gpg)
# generate key
key_input = gpg.gen_key_input()


key_ = gpg.gen_key(key_input)
print(key_
      )


