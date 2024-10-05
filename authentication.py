import csv
import bcrypt
import getpass
import validations
from log_functions import log

USER_FILE = 'users.csv'

def register():
    email = input("Enter your email: ")
    if not validations.validate_email(email):
        print("Invalid email format.")
        return
    password = getpass.getpass("Enter your password (invisible): ")
    if not validations.validate_password(password):
        print("Password does not meet criteria.")
        return
    confirm_password = input("Confirm your password (visible): ")
    if password != confirm_password:
        print("Passwords do not match.")
        return
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    security_question = input("Enter your security question (for password recovery): ")

    with open(USER_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([email, hashed_password.decode('utf-8'), security_question])

    log(f"New user registered: {email}")
    print("Registration successful!")

def login():
    email = input("Enter your email: ")
    if not validations.validate_email(email):
        print("Invalid email format.")
        return False
    password = getpass.getpass("Enter your password (invisible): ")
    with open(USER_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == email:
                hashed_password = row[1].encode('utf-8')
                if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                    log(f"User logged in: {email}")
                    print("Login successful!")
                    return True
                else:
                    print("Incorrect password.")
                    return False
    print("User not found.")
    return False

def reset_password():
    email = input("Enter your registered email: ")
    if not validations.validate_email(email):
        print("Invalid email format.")
        return

    user_found = False
    security_answer = ""
    with open(USER_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == email:
                user_found = True
                security_answer = row[2]  # Security question answer
                break

    if not user_found:
        print("Email not found.")
        return

    answer = input(f"Answer your security question '{security_answer}': ")
    if answer.strip() == "":
        print("Invalid answer.")
        return

    new_password = getpass.getpass("Enter your new password (invisible): ")
    if not validations.validate_password(new_password):
        print("New password does not meet criteria.")
        return
    confirm_new_password = input("Confirm your new password (visible): ")
    if new_password != confirm_new_password:
        print("Passwords do not match.")
        return

    hashed_new_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

    rows = []
    with open(USER_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == email:
                row[1] = hashed_new_password.decode('utf-8')
            rows.append(row)

    with open(USER_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    log(f"Password reset for user: {email}")
    print("Password reset successful!")
