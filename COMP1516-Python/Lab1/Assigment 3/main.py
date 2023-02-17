# Aline Hammermuller
# A01276569

import BankAccount as ba
import re


def main():
    try:
        print("creating a bank account")
        while True:
            username = input("enter the account holder name: ")
            account_balance = input("enter the balance: ")
            valid_name = re.search("^[a-zA-Z,\s,_,-]+$", username)
            valid_account_balance = re.search("^[0-9]+$", account_balance)
            information = ba.BankAccount(username, account_balance)
            if not valid_name or not valid_account_balance:
                continue
            else:
                break

        transaction = True
        while transaction:
            print("1 - deposit")
            print("2 - withdraw")
            choice = input("enter your choice: ")
            print(f'your choice is {choice}')
            if choice == "1":
                value = input("enter the amount to deposit: ")
                deposit = information.deposit(value)
                information.displayDetails(username, deposit)
            elif choice == "2":
                value = input("enter the amount to withdraw: ")
                withdraw = information.withdraw(value)
                information.displayDetails(username, withdraw)
            another_transaction = input("do you want to make another transaction?yes/no: ")
            if another_transaction == "no":
                transaction = False

    except ValueError as e:
        print(e)
        print("try again")
        main()


if __name__ == '__main__':
    main()


