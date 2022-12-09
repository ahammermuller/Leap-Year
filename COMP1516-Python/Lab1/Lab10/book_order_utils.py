# Aline Hammermuller
# A01276569

import re
import os

def validate_book_order_details(order_num, title, author, isbn, year, quantity, cost):
    """
    Function to validate the input pattern and handle exceptions.
    :param order_num:
    :param title:
    :param author:
    :param isbn:
    :param year:
    :param quantity:
    :param cost:
    :return:
    """
    order_pattern = "^[0-9]+$"
    if not re.search(order_pattern, order_num):
        raise ValueError("Order Number is invalid")

    title_pattern = "^[a-zA-Z' ]+$"
    if not re.search(title_pattern, title):
        raise ValueError("Title is invalid")

    author_pattern ="^[a-zA-Z' ]*$"
    if not re.search(author_pattern, author):
        raise ValueError("Author is invalid")

    isbn_pattern = "^[0-9]{4,20}$"
    if re.search(isbn_pattern, isbn):
        raise ValueError("ISBN is invalid")

    year_pattern = "^[0-9]{4}$"
    if not re.search(year_pattern, year):
        raise ValueError("Year is invalid")

    quantity_pattern = "^([0-9]|[1-9][0-9]{1,3}|1000)$"
    if not re.search(quantity_pattern, quantity):
        raise ValueError("Quantity is invalid")

    cost_pattern = "^^\d+.\d{2}$"
    if not re.search(cost_pattern, cost):
        raise ValueError("Cost is invalid")

    integer_pattern = "^[0-9]+$"
    if re.search(integer_pattern, isbn):
        raise TypeError("ISBN must be an integer")

    if not re.search(integer_pattern, year):
        raise TypeError("Year is invalid")

    if not re.search(integer_pattern, quantity):
        raise TypeError("Quantity must be an integer")


def calculate_per_book_cost(cost, quantity):
    """
    Function to calculate the cost by book unit.
    :param cost:
    :param quantity:
    :return: cost per book
    """
    cost_per_book = cost / quantity
    return cost_per_book


def write_book_order_details(filename, title, author, isbn, year, quantity, cost, unit_cost):
    """
    Function that takes some parameters and write it line by line in a text file handling an error if the filename
    already exists.
    :param filename:
    :param title:
    :param author:
    :param isbn:
    :param year:
    :param quantity:
    :param cost:
    :param unit_cost:
    :return:
    """

    if os.path.isfile(filename):
        raise ValueError("Order file name already exists!")
    else:
        f = open(filename, 'w')
        f.write(f'BOOK ORDER NUMBER {filename}\n')
        f.write(f'title = {title}\n')
        f.write(f'author = {author}\n')
        f.write(f'isbn = {isbn}\n')
        f.write(f'year = {year}\n')
        f.write(f'quantity = {quantity}\n')
        f.write(f'cost =${cost:.2f}\n')
        f.write(f'unit_cost =${unit_cost:.2f}\n')
        f.close()




