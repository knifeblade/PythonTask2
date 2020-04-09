import random
import string
title = "Employee details at HNG Tech"
print(title)


def get_registration():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    employee_email = input("Enter your email address: ")
    registration = [first_name, last_name, employee_email]
    return registration

def auto_password(registration):
    letters = string.ascii_letters
    pw_length = 5
    random_password = ''.join(random.choice(letters) for i in range(pw_length))
    password = str(registration[0][:2] + registration[1][-2:] + random_password)
    return password


condition = True
container = []
while condition:
    registration = get_registration()
    password = auto_password(registration)
    print(f"Your password is: str{password}")
    password_accept = input("Do you accept the given password. Enter Y or N: ")
    password_loop = True
    while password_loop:
        if password_accept.upper() == "Y":
            print("Congratulations! Registration Completed Successfully. ")
            registration.append(password)  # add accepted password to user details
            container.append(registration)  # add new user details to employee list container
            break
        else:
            user_password = input(str("Enter a new 7 character long password: "))
            password_len = True
            while password_len:
                if len(user_password) >= 7:
                    print("Congratulations! Registration Completed Successfully. ")
                    registration.append(password)  # add user's own password to user details
                    container.append(registration)  # add user's updated details to overall user details container
                    password_len = False
                    password_loop = False
                else:
                    print("Please enter a password with a minimum of 7 characters ")
                    user_password = input(str("Enter password: "))
    new_user = input(str("Are you registering another new user? Enter Y or N: "))
    if new_user.upper() == "N":
        condition = False
        for data in container:
            print(data)
    else:
        condition = True