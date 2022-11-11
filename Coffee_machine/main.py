import menu


def resources_report():
    """
    Function to print the total available resources (water, milk, coffee) and the total amount of money earned.
    """
    print(f'Water: {menu.resources["water"]}ml')
    print(f'Milk: {menu.resources["milk"]}ml')
    print(f'Coffee: {menu.resources["coffee"]}g')
    print(f'Money: ${profit}')


def sufficient_resources(ingredients):
    """
    Function to check if there are sufficient ingredients to make the coffee.
    :param ingredients:
    :return: true if the ingredients are sufficient or false if the ingredients are not sufficient.
    """
    sufficient_ingredients = True
    for item in ingredients:
        if ingredients[item] >= menu.resources[item]:
            print(f'Sorry there is not enough {item}')
            sufficient_ingredients = False
    return sufficient_ingredients


def process_coins():
    """
    Function to prompt to the user to enter the amount of coins (quarter, dime, nickel, and penny)
    and sum the total coins.
    :return: total amount of  coins
    """
    print("Please insert coins")
    total_quarter = int(input("How many quarters do you have?")) * 0.25
    total_dime = int(input("How many dimes do you have?")) * 0.10
    total_nickel = int(input("How many nickels do you have?")) * 0.05
    total_penny = int(input("How many pennies do you have?")) * 0.01
    total_coins = total_quarter + total_dime + total_nickel + total_penny
    return total_coins


def transaction_successful(money_received, drink_cost):
    """
    Function to check if the money payed is sufficient or not.
    :param money_received:
    :param drink_cost:
    :return: true if the money payed is sufficient or print a message in case of insufficient funds.
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(coffee, ingredients):
    for item in ingredients:
        menu.resources[item] -= ingredients[item]
    print(f'Here is your {coffee} ☕. Enjoy!')


def report():
    """
    Function to print a report
    """
    print(f'Water: {menu.resources["water"]}ml')
    print(f'Milk: {menu.resources["milk"]}ml')
    print(f'Coffee: {menu.resources["coffee"]}g')
    print(f'Money: ${profit}')


profit = 0


def main():
    is_on = True
    while is_on:
        desired_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if desired_coffee == "off":
            is_on = False
        elif desired_coffee == "report":
            report()
        else:
            drink = menu.menu[desired_coffee]
            if sufficient_resources(drink["ingredients"]):
                payment = process_coins()
                transaction_successful(payment, drink["cost"])
                make_coffee(desired_coffee, drink["ingredients"])


if __name__ == '__main__':
    main()
