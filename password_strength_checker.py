import string

password = input("Enter a password: ")

score = 0

if len(password) >= 8:
    score += 1

if any(char.isdigit() for char in password):
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char in string.punctuation for char in password):
    score += 1

if score == 4:
    print("Strong password")
elif score >= 2:
    print("Medium password")
else:
    print("Weak password")
