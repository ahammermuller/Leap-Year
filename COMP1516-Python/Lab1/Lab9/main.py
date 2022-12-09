# Aline Hammermuller
# A01276569

import re


def is_valid_bc_license_plate(plate):
    """
    Function to check is a license plate matches some requirements, and it is valid.
    :param plate:
    :return: True if it is a valid bc license plate. Otherwise, returns False.
    """
    valid_license = "^[A-Z]{3}\d{3}$|^\d{3}[A-Z]{3}$|^[A-Z]{2}\d[ -]?\d{2}[A-Z]$"

    if re.search(valid_license, plate):
        return True
    else:
        return False


def is_valid_python_variable_name(name):
    """
    Function to check is a variable name matches some requirements, and it is valid.
    :param name:
    :return: True if it is a valid variable name. Otherwise, returns False.
    """
    good_variable_name = "^[a-z_]{1,32}$"
    if re.search(good_variable_name, name):
        if not re.search("__", name):
            return True
    else:
        return False


def isValidEmailAddress(email):
    """
    Function to check if an email matches some requirements, and it is valid.
    :param email:
    :return: True if it is a valid email. Otherwise, return False.
    """
    email_data = re.split("@", email)
    username = email_data[0]
    domain_data = re.split("[.]", email_data[1])
    domain_name = domain_data[0]
    top_level_domain = domain_data[1]
    username_rule = "^[A-Za-z_]{1,256}"
    domain_name_rules = "^[A-Za-z]{1,32}"
    top_level_domain_rules = "[A-Za-z]{2,5}"
    if re.search(username_rule, username):
        if re.search(domain_name_rules, domain_name):
            if re.search(top_level_domain_rules, top_level_domain):
                return True
    else:
        return False


def main():
    print(is_valid_bc_license_plate("AB1 23C"))
    print(is_valid_python_variable_name("a_good_variable_name"))
    print(isValidEmailAddress("_Jason_Harrison_@bcit.ca"))


if __name__ == "__main__":
    main()