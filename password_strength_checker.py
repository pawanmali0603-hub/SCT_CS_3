import re

def check_password_strength(password):
    strength = 0
    remarks = []

    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        strength += 1
    else:
        remarks.append("Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks.append("Add at least one special character.")

    if strength == 5:
        print("\nPassword Strength: Strong 💪")
    elif strength >= 3:
        print("\nPassword Strength: Medium 👍")
    else:
        print("\nPassword Strength: Weak ❌")

    if remarks:
        print("\nSuggestions:")
        for remark in remarks:
            print("-", remark)

password = input("Enter your password: ")
check_password_strength(password)