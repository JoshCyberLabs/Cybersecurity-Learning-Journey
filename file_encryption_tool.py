from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

filename = input("Enter file name to encrypt: ")

key = get_random_bytes(16)

with open("secret.key", "wb") as key_file:
    key_file.write(key)

cipher = AES.new(key, AES.MODE_EAX)

with open(filename, "rb") as file:
    data = file.read()

ciphertext, tag = cipher.encrypt_and_digest(data)

with open(filename + ".encrypted", "wb") as encrypted_file:
    encrypted_file.write(cipher.nonce)
    encrypted_file.write(tag)
    encrypted_file.write(ciphertext)

print("File encrypted successfully!")
print("Keep secret.key safe to decrypt the file.")
