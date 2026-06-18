import hashlib

filename = input("Enter file name: ")

with open(filename, "rb") as file:
    data = file.read()

file_hash = hashlib.sha256(data).hexdigest()

print("File SHA-256 Hash:")
print(file_hash)
