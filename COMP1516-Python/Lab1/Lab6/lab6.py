
def weight_converter():
    """ Function to convert the weight in kilograms to weight in pounds from a range between 30kg and 100kg
    increasing by 10.
    """
    for kilos in range(30, 101, 10):
        kilo_in_pounds = kilos * 2.20
        print(f'Weight in kilos: {kilos} is {kilo_in_pounds:.2f} in Pounds')


def get_numbers_print_divisible():
    """
    Function that prompts to user enter three numbers being the last one is the divider, check which one of the two
    first numbers is greater and print the result of the division.
    If the divider is zero prints that it cannot be zero.
    If the first number is less than the second the function displays all between the first and the second inclusive
    that are divisible by the given divisor.
    If the first number is greater than the second the functions displays all the numbers between both on descending
    order.
    """
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    divisor = int(input("Enter the divisor number: "))
    if divisor == 0:
        print("the divisor cannot be 0")
        return
    elif number1 < number2:
        for number in range(number1, number2 + 1):
            if number % divisor == 0:
                print(number)
    elif number1 > number2:
        for number in range(number1, number2 - 1, -1):
            if number % divisor == 0:
                print(number)


def get_numbers_print_list_analysis():
    """
    Function that prompts to the user to type a positive integers or space to end the input. It stores the input into
    a list and in the end it prints the list, the quantity and the maximum and minimum numbers. Everything else that
    is not a positive integer is ignored by the function.
    """
    keep_looping = True
    positive_integers = []
    while keep_looping:
        number = input("Enter a positive integer: ")
        if number.isdigit() and int(number) >= 0:
            positive_integers.append(number)
        if number.isspace():
            keep_looping = False
    even_numbers = [digit for digit in positive_integers if int(digit) % 2 == 0]
    print(positive_integers)
    print("Quantity of items in the list: ", len(positive_integers))
    print("Quantity of even numbers in the list: ", len(even_numbers))
    positive_integers.sort()
    print("The minimum number is: ", positive_integers[0])
    print("The maximum number is: ", positive_integers[-1])


def calculate_total_pay_cad(number_of_employees, hourly_rate_cad):
    """
    Function prompts the user to enter the number of worked hours and creates a nested list with the number
    of worked hours and payment to each employee and prints it. If the employee worked less than 40 hours the payment
    calculation is just based on the hourly rate. If the employee works more than 40 hours what exceeds it is
    calculated taking into consideration the hourly rate times 1.5.
    :param number_of_employees:
    :param hourly_rate_cad:
    """
    employees_list = []
    while number_of_employees > len(employees_list):
        number_of_worked_hours = int(input("Input the number of worked hours "))
        if number_of_worked_hours <= 40:
            pay = number_of_worked_hours * hourly_rate_cad
            employees_list.append([number_of_worked_hours, pay])
        if number_of_worked_hours > 40:
            pay = 40 * hourly_rate_cad
            overtime_hours = number_of_worked_hours - 40
            overtime_rate = 1.5 * hourly_rate_cad
            total_pay = pay + (overtime_hours * overtime_rate)
            employees_list.append([number_of_worked_hours, total_pay])
    for hours, payment in employees_list:
        print(f'The employee worked for {hours} and earned {payment:.2f} $')


def is_prime(positive_number):
    """
    Function to check id a positive greater than 2 is prime or not.
    :param positive_number:
    :return: Flase if the number is not ptime or True if it is prime.
    """
    for i in range(2, positive_number):
        if (positive_number % i) == 0:
            return False
    return True


def display_prime_numbers(maximum):
    """
    Function generates a list of integers between 2 and a given number and display all the numbers that are prime in
    the list.
    :param maximum:
    """
    list_of_numbers = []
    for number in range(2, maximum + 1):
        list_of_numbers.append(number)
    print(list_of_numbers)
    for number in list_of_numbers:
        if is_prime(number):
            print(f'The number {number} is prime number.')


def main():
    weight_converter()
    get_numbers_print_divisible()
    get_numbers_print_list_analysis()
    employees = int(input("Enter the number of employees: "))
    hourly_rate_cad = float(input("Enter the hourly rate in CAD: "))
    calculate_total_pay_cad(employees, hourly_rate_cad)
    positive_integer = int(input("Enter a positive integer greater than 2: "))
    display_prime_numbers(positive_integer)


if __name__ == "__main__":
    main()
