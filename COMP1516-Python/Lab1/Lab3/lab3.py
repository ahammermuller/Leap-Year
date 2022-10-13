# Aline Hammermuller
# A01276569

import random


def loan_qualifier():
    """
    Function to calculate if a person qualifies to a loan based on the annual income and years employed.
    It prompts to the user monthly salary and the number of years employed and calculate the annual income.
    If the annual income is more than 50000 and the user is employed for more than 3 years it displays that
    the user qualifies to a load. Otherwise, displays that the user needs a higher income or be employed for more
    than 3 years and do not qualify for a loan.
    """
    monthly_salary = float(input("Enter your monthly salary: "))
    years_employed = float(input("Enter the number of years employed: "))
    annual_income = monthly_salary * 12
    if annual_income >= 50000 and years_employed >= 3:
        print("you qualify for a loan.")
    if annual_income < 50000:
        print("your income must be 50000 or more, you don’t qualify for a loan.")
    if years_employed < 3:
        print("you must be employed for 3 years or more, you don’t qualify for a loan.")


def calculate_montly_cell_phone_bill_charge_cad(air_time_minutes_amount, text_messages_amount):
    """
    Function to calculate the monthly bill.
    It displays the base charge, additional minutes charge (if any), additional text messages charge(if any),
    the 911 fee, the tax and the total bill charge.
    :param air_time_minutes_amount:
    :param text_messages_amount:
    """
    if air_time_minutes_amount < 0 or text_messages_amount < 0:
        print("Invalid minutes or messages amount")
        return
    base_charge = 15.0
    nine_one_one_fee = 0.44
    additional_minutes_charge = 0
    additional_text_messages_charge = 0
    print("Base charge is: ", base_charge)
    if air_time_minutes_amount > 50:
        additional_minutes_charge = (air_time_minutes_amount - 50) * 0.25
        print("Additional minutes charge is: ", additional_minutes_charge)
    if text_messages_amount > 50:
        additional_text_messages_charge = (text_messages_amount - 50) * 0.15
        print("Additional text messages charge is: ", additional_text_messages_charge)
    print("911 service fee: ", nine_one_one_fee)
    total_sales = base_charge + nine_one_one_fee + additional_minutes_charge + additional_text_messages_charge
    sales_tax = total_sales * 0.05
    print("Tax amount: ", sales_tax)
    total_charge = sales_tax + total_sales
    print("Total charge is: ", total_charge)


def get_square_colour(row_number, column_character):
    """
    Function to display if the square colour is White or Black according to the given parameters.
    :param row_number:
    :param column_character:
    """
    if row_number % 2 == 0:
        if column_character == "a" or column_character == "c" or column_character == "e" or column_character == "g":
            print("White square")
        else:
            print("Black_square")
    if row_number % 2 == 1:
        if column_character == "b" or column_character == "d" or column_character == "f" or column_character == "h":
            print("White square")
        else:
            print("Black_square")


def play_chicago():
    """
    Function to implement the Chicago game. The game has 11 rounds and in each one a random number between 1 and 6
    is generated. If the sum of this two numbers is equals to the round number the user wins a point.
    In the end of each round the user is able to play again. If the answer is no or the round is number 12
    the program displays the points earned.
    """
    round_number = 2
    play_another_round = "yes"
    points = 0
    while round_number < 13 and play_another_round == "yes":
        number1 = random.randint(1, 6)
        number2 = random.randint(1, 6)
        print("Round number:", round_number)
        print("First dice number is: ", number1)
        print("Second dice number is: ", number2)
        if number1 + number2 == round_number:
            points += 1
            print("You won a point. Your current points are: ", points)
        else:
            print("No points. Your current points are: ", points)
        play_another_round = input("Do you want to play again? enter \"yes\" to continue ")
        round_number += 1
    print("The game is over. You earned", points, "points.")


def main():
    loan_qualifier()
    calculate_montly_cell_phone_bill_charge_cad(60, 60)
    get_square_colour(1, "a")
    play_chicago()


if __name__ == "__main__":
    main()
