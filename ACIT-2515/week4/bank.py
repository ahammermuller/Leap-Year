#Aline Hammermuller
#A01276569

from customer import Customer
from account import Account, CreditAccount, SavingsAccount

class Bank:
    def __init__(self, name):
        self.name = name
        self._balance = 0.0
        self.accounts = list()

    
    def create_account(self, category, owner: Customer,  interest_rate = 0):
        """Create accounts such as account, credit or savings"""
        self.owner = owner
        self.category = category
        self.interest = interest_rate

        if category == "account":
            bank_account = Account(owner)

        if category == "credit":
            bank_account = CreditAccount(owner, interest_rate)

        if category == "savings":
            bank_account = SavingsAccount(owner, interest_rate)

        self.accounts.append(bank_account)
        return bank_account

    def find_accounts_by_name(self, name):
        """Find accounts by name"""
        accountsList = list()
        for info in self.accounts:
            if info.owner.name == name:
                accountsList.append(info)
        return accountsList


    def find_accounts_by_ssn(self, ssn):
        """Find accounts by ssn"""
        accountsList = list()
        for info in self.accounts:
            if info.owner.ssn == ssn:
                accountsList.append(info)
        return accountsList

    @property
    def balance(self):
        total = 0
        for account in self.accounts:
            total += account.amount
        return total

    @balance.setter
    def balance(self, value):
        ac = Account(self.owner)
        cd = CreditAccount(self.owner, interest_rate=0)
        sv = SavingsAccount(self.owner)
        value = ac._amount + cd._amount + sv._amount
        self._balance = value
