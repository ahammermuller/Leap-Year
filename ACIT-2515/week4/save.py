class Bank:
    def __init__(self, name):
        self.name = name
        self._amount = 0.0
        self.accounts = dict()

    
    def create_account(self, category, owner: Customer,  interest_rate = 0):
        self.owner = owner
        self.category = category
        self.interest = interest_rate

        self.accounts[self.owner.name] = list()

        if category == "account":
            account = Account(owner)
            self.accounts[self.owner.name].append(account)
            return account

        if category == "credit":
            credit = CreditAccount(owner, interest_rate)
            self.accounts[self.owner.name].append(credit)
            return credit

        if category == "savings":
            saving = SavingsAccount(owner, interest_rate)
            self.accounts[self.owner.name].append(saving)
            return saving
        

    def find_accounts_by_name(self, name):
        accountsList = []
        name = name.title()
        for key, value in self.accounts.items():
            if name in key:
                accountsList.append(value)
        return accountsList


    def find_accounts_by_ssn(self, name):
        accountsList = []
        name = name.title()
        for key, value in self.accounts.items():
            if name in key:
                accountsList.append(value)
        return accountsList


    @property
    def balance(self):
        return self._amount

    @balance.setter
    def balance(self,value):
        if value < 0:
            raise ValueError("Invalid amount")
        self._amount = value
