# Aline Hammermuller
# A01276569
import re


class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        if not re.search(".+", name):
            raise ValueError("Name cannot be empty")
        if re.search("[^A-Za-z\s]+", name):
            raise ValueError("Name cannot include numbers or symbols")
        if balance < 0:
            raise ValueError("Balance cannot be negative")
    
    def displayDetails(self):
        """
        Function to display the account holder and account balance.
        """
        print(f'Name is: {self.name}')
        print(f'Balance is: {self.balance}')

    def deposit(self, amount):
        """
        Function to sum the deposit amount to the account balance.
        :param amount:
        :return: balance
        """
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount cannot be zero or less")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        Function to deduce the amount to withdraw from the balance.
        :param amount:
        :return: balance
        """
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount cannot be zero or less than zero")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance




