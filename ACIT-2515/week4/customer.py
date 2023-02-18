class Customer:
    def __init__(self, name, ssn):
        if type(name) is not str or len(name) < 2:
            raise AttributeError("Invalid name")
        
        if type(ssn) is not str or not ssn.isnumeric():
            raise AttributeError("Invalid SSN")

        self.name = name
        self.ssn = ssn