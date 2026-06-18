password = input("Enter a password: ")

if len(password) < 8:
    print("Weak password: Use at least 8 characters")
elif password.isalpha() or password.isdigit():
    print("Weak password: Mix letters and numbers")
else:
    print("Strong password")
