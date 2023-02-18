#Aline Hammermuller
#A01276569

from customer import Customer

class Account:
    def __init__(self, owner):
        if type(owner) is str:
            raise AttributeError("Invalid customer")
        self.owner = owner
        self.amount = 0.0
    
    def deposit(self, value):
        """Deposit a value"""
        if value < 0: 
            raise AttributeError("Negative amount.")
        self.amount += value
    
    def withdraw(self, value):
        """Withdraw a value"""
        if value < 0:
            raise AttributeError("Negative withdraw amount.")
        self.amount -= value

    def transfer(self, other_account, amount):
        """Transfer amounts from one account to another"""
        if not isinstance(other_account ,Account) :
            raise TypeError("Invalid account type")
        self.withdraw(amount) 
        other_account.deposit(amount)

    def compute_interest(self):
        """Compute interest when need"""
        pass


    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount=value


class CreditAccount(Account):
    def __init__(self, owner, interest_rate):
        super().__init__(owner)        
        self.interest = interest_rate

    def compute_interest(self):
        """Compute interest when negative amount"""
        if self.amount < 0:
            self.amount = (self.amount * (100 + self.interest) / 100) - 10

class SavingsAccount(Account):
    def __init__(self, owner, interest_rate = 0):
        super().__init__(owner)        
        self.interest = interest_rate

    def compute_interest(self):
        """Compute interest"""
        self.amount = amount = amount * (100 + self.interest) / 100
    
    def withdraw(self, value):
        """Withdraw a value"""
        if value > self.amount:
            raise UserWarning("You don't have this amount in your bank account")
        self.amount -= value


if __name__ == 'main':
    
    customer = Customer("Tim", "84093232")
    ac = Account(customer)
    ac.deposit(1000)
    print(ac._amount)
    