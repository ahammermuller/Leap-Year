# Aline Hammermuller
# A01276569

import re


def isFloat(number):
    """
    Function to check if a number is a float and return true or false
    :param number: a string representing a number
    :return: True if the string can be interpreted as a float, False otherwise
    """
    if not number:  # empty string is not a float
        return False
    if number.count('.') != 1:  # a float must have exactly one decimal point
        return False
    for i, c in enumerate(number):
        if i == 0 and c in '+-':  # optional sign at the beginning
            continue
        if not c.isdigit() and c != '.':  # every character must be a digit or decimal point
            return False
        if c == '.' and i == len(number) - 1:  # decimal point must not be the last character
            return False
    return True



students = {
    "Bob": {
        "name": "Bob",
        "homework": [90.0, 97.0, 75.0, 82.0],
        "quizzes": [88.0, 40.0, 54.0],
        "assignments": [75.0, 90.0, 83.0, 62.0]},
    "Jane": {
        "name": "Jane",
        "homework": [100.0, 92.0, 98.0, 95.0],
        "quizzes": [82.0, 83.0, 91.0],
        "assignments": [89.0, 97.0]},
    "Max": {
        "name": "Max",
        "homework": [0.0, 87.0, 75.0, 22.0],
        "quizzes": [0.0, 75.0, 78.0],
        "assignments": [100.0, 100.0]}
            }


def average(numbers):
    total = sum(numbers)
    return float(total) / len(numbers)


def calculate_average():
    """
    Function to calculate and add average values to each student's dictionary entry
    """
    for student in students.values():
        homework_avg = sum(student['homework']) / len(student['homework'])
        quizzes_avg = sum(student['quizzes']) / len(student['quizzes'])
        assignments_avg = sum(student['assignments']) / len(student['assignments'])
        final_avg = (homework_avg + quizzes_avg + assignments_avg) / 3
        student['homework_average'] = homework_avg
        student['quizzes_average'] = quizzes_avg
        student['assignments_average'] = assignments_avg
        student['final_average'] = final_avg


def display_student_details():
    """
    Function to display each student's information
    """
    for student in students.values():
        print(student['name'])
        print(f"Homework average: {student['homework_average']:.2f}")
        print(f"Quizzes average: {student['quizzes_average']:.2f}")
        print(f"Assignments average: {student['assignments_average']:.2f}")
        print(f"Final average: {student['final_average']:.2f}")
        print()  # print an empty line for readability


import re

def add_property():
    """
    Function to user input data about property that checks if it matches the required patterns and if yes, add it to
    a dictionary.
    :return: none
    """
    try:
        property_details = {}
        msl_pattern = "^[A-Z]\d{5,7}"
        msl_number = input("please insert the MSL Number: ")
        if not re.search(msl_pattern, msl_number):
            raise ValueError("The MLS number is invalid")

        address_pattern = "^[a-zA-Z0-9\s,.-]+"
        address = input("Please insert the address: ")
        if not re.search(address_pattern, address):
            raise ValueError("The address is invalid")

        owner_pattern = "^[a-zA-Z\s]+"
        owner_name = input("Please insert the owner’s name: ")
        if not re.search(owner_pattern, owner_name):
            raise ValueError("The owner's name is invalid")

        bedrooms_pattern = "^[0-9]+"
        num_bedrooms = input("Please insert the number of bedrooms: ")
        if not re.search(bedrooms_pattern, num_bedrooms):
            raise ValueError("The number of bedrooms must be digits")

        property_description = input("Please insert the property description: ")

        property_details['msl_number'] = msl_number
        property_details['address'] = address
        property_details['owner_name'] = owner_name
        property_details['number_of_bedrooms'] = num_bedrooms
        property_details['property_description'] = property_description
        print(property_details)

    except ValueError as e:
        print(e)



def main():
    print(isFloat('-234.345'))  # True
    print(isFloat('123.123.123'))  # False
    print(isFloat('+456.33'))  # True
    print(isFloat('567.5'))  # True
    print(isFloat('+-456.322'))  # False
    print(isFloat('++456.67778'))  # False
    print(isFloat('4553.0'))  # True
    print(isFloat('345.'))  # False In the math definition they are float
    print(isFloat('55667'))  # False In the math definition they are float
    print(isFloat('.4567'))  # False In the math definition they are float
    print(isFloat('0.456'))  # True
    print(isFloat('comp1516'))  # False

    calculate_average()
    display_student_details()
    add_property()


if __name__ == '__main__':
    main()


