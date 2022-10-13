# Aline Hammermuller
# A01276569


def get_retail_item_description():
    """
    Function to prompt the user to enter the retail item description.
    :return: item_description
    """
    item_description = input("Enter the retail item description: ")
    return item_description


def get_number_of_purchased_items ():
    """
    Function to prompt the user to enter the quantity sold.
    :return: quantity_sold
    """
    quantity_sold = int(input("Enter the quantity purchased: "))
    return quantity_sold


def get_price_per_unit():
    """
    Function to prompt the user to type the price per unit.
    :return: price
    """
    unit_price = float(input("Enter the price: per unit: "))
    return unit_price


def get_tax_rate():
    """
    Function to prompt the user to enter the tax rate as a floating point.
    :return: tax_rate
    """
    tax_rate = float(input("Enter the tax rate as a float number: "))
    return tax_rate


def calculate_subtotal(price, quantity_sold):
    """
    Function to calculate the subtotal by multiplying the price per unit by the quantity purchased.
    :param price:
    :param quantity_sold:
    :return: subtotal_amount
    """
    subtotal_amount = price * quantity_sold
    return subtotal_amount


def calculate_tax(subtotal, tax):
    """
    Function to calculate the tax amount of the subtotal by multiplying the subtotal byt the tax.
    :param subtotal:
    :param tax:
    :return: tax_amount
    """
    tax_amount = subtotal * tax
    return tax_amount


def calculate_total(subtotal, tax):
    """Function to calculate de total amount by summing the subtotal and tax amount.
    :param subtotal:
    :param tax:
    :return: total_tax_amount
    """
    total_amount = subtotal + tax
    return total_amount


def main():
    """This function is to display a sales receipt. This receipt includes the item description, quantity sold,
    price and tax. It also displays the calculated amount for subtotal, tax amount and the total.
    """
    item = get_retail_item_description()
    number_items = get_number_of_purchased_items()
    price = get_price_per_unit()
    tax = get_tax_rate()
    subtotal_price = calculate_subtotal(price, number_items)
    subtotal_tax = calculate_tax(subtotal_price, tax)
    total = calculate_total(subtotal_price, subtotal_tax)
    print("Sales Receipt:")
    print("Item description: ", item)
    print("Number of Purchased items: ", number_items)
    print("Unit price: ", price)
    print("Tax Rate: ", tax)
    print("Subtotal: ", subtotal_price)
    print("Tax: ", subtotal_tax)
    print("Total: ", total)


if __name__ == '__main__':
    main()
