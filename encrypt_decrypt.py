
choose_opt = input("Please choose (1. Encrypt 2. Decrypt) : ")
if choose_opt == "1":
    exec(open("genarate_key/encrypt_file.py").read())
else:
    exec(open("genarate_key/decrypt_file.py").read())


