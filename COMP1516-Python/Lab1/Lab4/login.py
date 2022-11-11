
def generate_login(first_name, last_name, bcit_id):
    """
    Function that gets the first three letters of the user first name, first three letters of last name and the last
    three letters of their BCIT ID. After properly format it a default login password is generated.
    :param first_name:
    :param last_name:
    :param bcit_id:
    :return: default login password
    """
    formatted_first_name = first_name.title()
    formatted_last_name = last_name.title()
    default_login_password = formatted_first_name[:3] + formatted_last_name[:3] + bcit_id[-3:]
    return default_login_password


def has_upper(password):
    """
    Function to check if there is any uppercase character in a password. If not displays a message to the user
    informing that the password must have at least one uppercase character.
    :param password:
    :return: True or False
    """
    if any(character.isupper() for character in password):
        return True
    else:
        print("The password must have at least one uppercase character")
        return False


def has_lower(password):
    """
    Function to check if there is any lowercase character in a password. If not displays a message to the user
    informing that the password must have at least one lowercase character.
    :param password:
    :return: True or False
    """
    if any(character.islower() for character in password):
        return True
    else:
        print("The password must have at least one lowercase character.")
        return False


def has_num(password):
    """
    Function to check if there is any number in a password. If not displays a message to the user
    informing that the password must have at least one number.
    :param password:
    :return: True or False
    """
    if any(character.isdigit() for character in password):
        return True
    else:
        print("The password must have at least one number.")
        return False


def has_special_char(password):
    """
    Function to check if there is any special character in a password. If not displays a message to the user
    informing that special characters are not allowed.
    :param password:
    :return: True or False
    """
    special_character = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<',
                         '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
    if not any(character in special_character for character in password):
        return True
    else:
        print("Special characters are not allowed.")
        return False


def change_password():
    """
    Function that prompts the user to enter a new password checking if the password meets the specifications.
    :return: valid password
    """
    print("Enter a new password. The password should be at least 7 characters long, has one upper case, one lower case "
          "character and one number. It cannot have special characters.")
    valid_password = ""
    password_validation = True
    while password_validation:
        new_password = input("Enter a new password: ")
        if len(new_password) > 7 and has_lower(new_password) and has_upper(new_password) and has_num(new_password) and has_special_char(new_password):
            password_validation = False
            valid_password = new_password
    return valid_password
